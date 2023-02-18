import asyncio
import base64
import binascii
import hashlib
import hmac
import json
from struct import pack
from typing import (
    Dict,
    Optional,
)

import rsa
from aiohttp import FormData
from bitstring import BitArray
from yarl import URL

from pysteamauth.abstract import (
    CookieStorageAbstract,
    RequestStrategyAbstract,
)
from pysteamauth.base import BaseRequestStrategy
from pysteamauth.pb.enums_pb2 import k_ESessionPersistence_Persistent
from pysteamauth.pb.steammessages_auth.steamclient_pb2 import (
    CAuthentication_BeginAuthSessionViaCredentials_Request,
    CAuthentication_BeginAuthSessionViaCredentials_Response,
    CAuthentication_GetPasswordRSAPublicKey_Request,
    CAuthentication_GetPasswordRSAPublicKey_Response,
    CAuthentication_UpdateAuthSessionWithSteamGuardCode_Request,
    CAuthentication_UpdateAuthSessionWithSteamGuardCode_Response,
    EAuthSessionGuardType,
    EAuthTokenPlatformType,
    k_EAuthSessionGuardType_DeviceCode,
    k_EAuthTokenPlatformType_WebBrowser,
)

from .helpers import (
    generate_sessionid,
    get_cookies,
    get_website_id_by_platform,
    pbmessage_to_request,
)
from .schemas import LoginResult
from .steambase import BaseSteam


class SteamServerTime:

    _requests = BaseRequestStrategy(
        raise_for_status=True,
    )

    @classmethod
    async def get_time(cls) -> int:
        response = await cls._requests.text(
            method='POST',
            url='https://api.steampowered.com/ITwoFactorService/QueryTime/v0001',
        )
        return int(json.loads(response)['response']['server_time'])


class Steam(BaseSteam):

    def __init__(
        self,
        login: str,
        password: str,
        steamid: Optional[int] = None,
        shared_secret: Optional[str] = None,
        identity_secret: Optional[str] = None,
        device_id: Optional[str] = None,
        cookie_storage: Optional[CookieStorageAbstract] = None,
        request_strategy: Optional[RequestStrategyAbstract] = None,
        platform: EAuthTokenPlatformType = k_EAuthTokenPlatformType_WebBrowser,
    ):
        super().__init__(request_strategy, cookie_storage)
        self._login = login
        self._steamid = steamid
        self._password = password
        self._shared_secret = shared_secret
        self._identity_secret = identity_secret
        self._device_id = device_id
        self._platform = platform

    @property
    def steamid(self) -> int:
        if self._steamid is None:
            raise ValueError('steamid is not specified')
        return self._steamid

    @property
    def shared_secret(self) -> Optional[str]:
        return self._shared_secret

    @property
    def identity_secret(self) -> Optional[str]:
        return self._identity_secret

    @property
    def device_id(self) -> Optional[str]:
        return self._device_id

    @property
    def login(self) -> str:
        return self._login

    @property
    def partner_id(self) -> int:
        return self.steamid - 76561197960265728

    async def cookies(self, domain: str = 'steamcommunity.com') -> Dict[str, str]:
        return await self._storage.get(
            key=self._login,
            platform=self._platform,
            domain=domain,
        )

    async def _getrsakey(self) -> CAuthentication_GetPasswordRSAPublicKey_Response:
        message = CAuthentication_GetPasswordRSAPublicKey_Request(
            account_name=self._login,
        )
        response = await self._requests.bytes(
            method='GET',
            url='https://api.steampowered.com/IAuthenticationService/GetPasswordRSAPublicKey/v1',
            params={
                'input_protobuf_encoded': pbmessage_to_request(message),
            },
        )
        return CAuthentication_GetPasswordRSAPublicKey_Response.FromString(response)

    async def _begin_auth_session_via_credentials(
            self,
            encrypted_password: str,
            rsa_timestamp: int,
    ) -> CAuthentication_BeginAuthSessionViaCredentials_Response:
        message = CAuthentication_BeginAuthSessionViaCredentials_Request(
            account_name=self._login,
            encrypted_password=encrypted_password,
            encryption_timestamp=rsa_timestamp,
            remember_login=True,
            platform_type=self._platform,
            website_id=get_website_id_by_platform(self._platform),
            persistence=k_ESessionPersistence_Persistent,
        )
        response = await self._requests.bytes(
            method='POST',
            url='https://api.steampowered.com/IAuthenticationService/BeginAuthSessionViaCredentials/v1',
            data=FormData(
                fields=[
                    ('input_protobuf_encoded', pbmessage_to_request(message)),
                ],
            ),
        )
        return CAuthentication_BeginAuthSessionViaCredentials_Response.FromString(response)

    @classmethod
    async def get_steam_guard(cls, shared_secret: str, server_time: int) -> str:
        data = binascii.unhexlify(
            hmac.new(
                key=base64.b64decode(shared_secret),
                msg=pack('!L', 0) + pack('!L', server_time // 30),
                digestmod=hashlib.sha1,
            ).hexdigest(),
        )

        value = data[19] & 0xF
        fullcode = (
            (data[value] & 0x7F) << 24 |       # noqa:W504
            (data[value + 1] & 0xFF) << 16 |   # noqa:W504
            (data[value + 2] & 0xFF) << 8 |    # noqa:W504
            (data[value + 3] & 0xFF)
        )

        code = ''
        chars = '23456789BCDFGHJKMNPQRTVWXY'
        for _ in range(5):
            code += chars[fullcode % len(chars)]
            fullcode //= len(chars)

        return code

    def get_confirmation_hash(self, server_time: int, tag: str = 'conf') -> str:
        if self._identity_secret is None:
            raise ValueError('identity_secret is not specified')
        identitysecret = base64.b64decode(
            self._identity_secret,
        )
        secret = BitArray(
            bytes=identitysecret,
            length=len(identitysecret) * 8,
        )
        tag_buffer = BitArray(
            bytes=tag.encode('utf8'),
            length=len(tag) * 8,
        )
        buffer = BitArray(4 * 8)
        buffer.append(BitArray(int=server_time, length=32))
        buffer.append(tag_buffer)
        confirmation = hmac.new(
            key=secret.tobytes(),
            msg=buffer.tobytes(),
            digestmod=hashlib.sha1,
        )
        return str(base64.b64encode(confirmation.digest()), 'utf8')

    def _encrypt_password(self, keys: CAuthentication_GetPasswordRSAPublicKey_Response) -> str:
        publickey_exp = int(keys.publickey_exp, 16)  # type:ignore
        publickey_mod = int(keys.publickey_mod, 16)  # type:ignore
        public_key = rsa.PublicKey(
            n=publickey_mod,
            e=publickey_exp,
        )
        encrypted_password = rsa.encrypt(
            message=self._password.encode('ascii'),
            pub_key=public_key,
        )
        return str(base64.b64encode(encrypted_password), 'utf8')

    async def _update_auth_session_with_steam_guard(
            self,
            client_id: int,
            steamid: int,
            code: str,
            code_type: EAuthSessionGuardType,
    ) -> CAuthentication_UpdateAuthSessionWithSteamGuardCode_Response:
        message = CAuthentication_UpdateAuthSessionWithSteamGuardCode_Request(
            client_id=client_id,
            steamid=steamid,
            code=code,
            code_type=code_type,
        )
        response = await self._requests.bytes(
            method='POST',
            url='https://api.steampowered.com/IAuthenticationService/UpdateAuthSessionWithSteamGuardCode/v1',
            data=FormData(
                fields=[
                    ('input_protobuf_encoded', pbmessage_to_request(message)),
                ],
            ),
        )
        return CAuthentication_UpdateAuthSessionWithSteamGuardCode_Response.FromString(response)

    async def _confirm_authorization(self, session: CAuthentication_BeginAuthSessionViaCredentials_Response) -> None:
        """
        Confirmation authorization via Steam Guard
        """
        if session.allowed_confirmations[0].confirmation_type != k_EAuthSessionGuardType_DeviceCode:
            return
        if self._shared_secret is None:
            raise ValueError('shared_secret is not specified')
        code = await Steam.get_steam_guard(
            shared_secret=self._shared_secret,
            server_time=await SteamServerTime.get_time()
        )
        await self._update_auth_session_with_steam_guard(
            client_id=session.client_id,
            steamid=session.steamid,
            code=code,
            code_type=k_EAuthSessionGuardType_DeviceCode,
        )

    async def login_to_steam(self, force: bool = False) -> Optional[LoginResult]:
        """
        Login to Steam.
        """
        if await self.is_alive_session() and not force:
            return None
        self._requests.cookies.clear()
        keys = await self._getrsakey()
        password = self._encrypt_password(keys)
        session = await self._begin_auth_session_via_credentials(password, keys.timestamp)
        if session.allowed_confirmations:
            await self._confirm_authorization(session)

        session_status = await self._poll_auth_session_status(
            client_id=session.client_id,
            request_id=session.request_id,
        )
        tokens = await self._finalize_login(
            refresh_token=session_status.refresh_token,
            sessionid=generate_sessionid(),
        )
        # Need to authorize subdomains
        await self._set_tokens(int(tokens.steamID), tokens.transfer_info)
        # Need to authorize domains and receive additional cookies
        await asyncio.gather(*[
            self._requests.request(URL(token.url).origin(), 'GET') for token in tokens.transfer_info
        ])
        await self._storage.set(
            key=self._login,
            platform=self._platform,
            cookies=get_cookies(self._requests.cookies),
        )
        return LoginResult(
            client_id=session.client_id,
            refresh_token=session_status.refresh_token,
            access_token=session_status.access_token,
        )
