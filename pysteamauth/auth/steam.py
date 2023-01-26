import base64
import hashlib
import hmac
import json
from typing import (
    Any,
    Mapping,
    Optional,
)

import rsa
from aiohttp import FormData
from bitstring import BitArray
from urllib3.util import parse_url

from pysteamauth.abstract import (
    CookieStorageAbstract,
    RequestStrategyAbstract,
)
from pysteamauth.pb.enums_pb2 import ESessionPersistence
from pysteamauth.pb.steammessages_auth.steamclient_pb2 import (
    CAuthentication_AllowedConfirmation,
    CAuthentication_BeginAuthSessionViaCredentials_Request,
    CAuthentication_BeginAuthSessionViaCredentials_Response,
    CAuthentication_GetPasswordRSAPublicKey_Request,
    CAuthentication_GetPasswordRSAPublicKey_Response,
    CAuthentication_UpdateAuthSessionWithSteamGuardCode_Request,
    EAuthSessionGuardType,
    EAuthTokenPlatformType,
)

from ..base import BaseRequestStrategy
from .steambase import BaseSteam
from .utils import pbmessage_to_request


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
    ):
        super().__init__(request_strategy, cookie_storage)
        self._login = login
        self._steamid = steamid
        self._password = password
        self._shared_secret = shared_secret
        self._identity_secret = identity_secret
        self._device_id = device_id

    @property
    def steamid(self) -> int:
        if not self._steamid:
            raise ValueError('steamid is not specified')
        return self._steamid

    @property
    def shared_secret(self) -> str:
        if not self._shared_secret:
            raise ValueError('shared_secret is not specified')
        return self._shared_secret

    @property
    def identity_secret(self) -> str:
        if not self._identity_secret:
            raise ValueError('identity_secret is not specified')
        return self._identity_secret

    @property
    def device_id(self) -> str:
        if not self._device_id:
            raise ValueError('device_id is not specified')
        return self._device_id

    @property
    def login(self) -> str:
        return self._login

    @property
    def partner_id(self) -> int:
        return self.steamid - 76561197960265728

    async def cookies(self, domain: str = 'steamcommunity.com') -> Mapping[str, str]:
        return await self._storage.get(
            login=self._login,
            domain=domain,
        )

    async def sessionid(self, domain: str = 'steamcommunity.com') -> str:
        return (await self.cookies(domain))['sessionid']

    async def request(self, url: str, method: str = 'GET', **kwargs: Any) -> str:
        cookies = await self._storage.get(
            login=self._login,
            domain=parse_url(url).host,
        )
        return await self._requests.text(
            url=url,
            method=method,
            cookies={
                **cookies,
                **kwargs.pop('cookies', {}),
            },
            **kwargs,
        )

    async def is_authorized(self) -> bool:
        response: str = await self.request(
            url='https://steamcommunity.com/chat/clientjstoken',
        )
        data = json.loads(response)
        logged_in = data['logged_in']
        if logged_in:
            if not self._steamid:
                try:
                    self._steamid = int(data['steamid'])
                except KeyError:
                    ...
        return logged_in

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

    async def _begin_auth_session(
            self,
            encrypted_password: str,
            rsa_timestamp: int,
    ) -> CAuthentication_BeginAuthSessionViaCredentials_Response:
        message = CAuthentication_BeginAuthSessionViaCredentials_Request(
            account_name=self._login,
            encrypted_password=encrypted_password,
            encryption_timestamp=rsa_timestamp,
            remember_login=True,
            platform_type=EAuthTokenPlatformType.k_EAuthTokenPlatformType_WebBrowser,
            website_id='Community',
            persistence=ESessionPersistence.k_ESessionPersistence_Persistent,
            device_friendly_name='Mozilla/5.0 (X11; Linux x86_64; rv:1.9.5.20) Gecko/2812-12-10 04:56:28 Firefox/3.8',
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
        sharedsecret = base64.b64decode(shared_secret)
        secret = BitArray(
            bytes=sharedsecret,
            length=len(sharedsecret) * 8,
        )
        buffer = BitArray(8 * 8)
        buffer[4 * 8:] = int(server_time // 30)
        signature = hmac.new(
            key=secret.tobytes(),
            msg=buffer.tobytes(),
            digestmod=hashlib.sha1,
        ).digest()
        hashed = BitArray(
            bytes=signature,
            length=len(signature) * 8,
        )
        start = hashed[(19 * 8):(19 * 8) + 8] & BitArray('0x0f')
        slice_ = hashed[start.int * 8:(start.int * 8) + (4 * 8)]
        fullcode = (slice_ & BitArray("0x7fffffff")).int
        symbols = '23456789BCDFGHJKMNPQRTVWXY'
        code = ''
        for _ in range(5):
            code += symbols[int(fullcode % len(symbols))]
            fullcode = fullcode / len(symbols)
        return code

    def get_confirmation_hash(self, server_time: int, tag: str = 'conf') -> str:
        identitysecret = base64.b64decode(
            self.identity_secret,
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

    async def _update_auth_session(
            self,
            client_id: int,
            steamid: int,
            code: str,
            code_type: EAuthSessionGuardType,
    ) -> None:
        message = CAuthentication_UpdateAuthSessionWithSteamGuardCode_Request(
            client_id=client_id,
            steamid=steamid,
            code=code,
            code_type=code_type,
        )
        await self._requests.request(
            method='POST',
            url='https://api.steampowered.com/IAuthenticationService/UpdateAuthSessionWithSteamGuardCode/v1',
            data=FormData(
                fields=[
                    ('input_protobuf_encoded', pbmessage_to_request(message)),
                ],
            ),
        )

    def _is_twofactor_required(self, confirmation: CAuthentication_AllowedConfirmation) -> bool:
        return confirmation.confirmation_type == EAuthSessionGuardType.k_EAuthSessionGuardType_DeviceCode

    async def login_to_steam(self) -> None:
        if await self.is_authorized():
            return
        if not self._requests.cookies().get('sessionid'):
            await self._requests.bytes(
                method='GET',
                url='https://steamcommunity.com',
            )
        keys = await self._getrsakey()
        encrypted_password = self._encrypt_password(keys)
        auth_session = await self._begin_auth_session(
            encrypted_password=encrypted_password,
            rsa_timestamp=keys.timestamp,
        )
        if auth_session.allowed_confirmations:
            if self._is_twofactor_required(auth_session.allowed_confirmations[0]):
                server_time = await SteamServerTime.get_time()
                code = await Steam.get_steam_guard(self.shared_secret, server_time)
                await self._update_auth_session(
                    client_id=auth_session.client_id,
                    steamid=auth_session.steamid,
                    code=code,
                    code_type=EAuthSessionGuardType.k_EAuthSessionGuardType_DeviceCode,
                )
        session = await self._poll_auth_session_status(
            client_id=auth_session.client_id,
            request_id=auth_session.request_id,
        )
        tokens = await self._finalize_login(
            refresh_token=session.refresh_token,
            sessionid=self._requests.cookies()['sessionid'],
        )
        for token in tokens.transfer_info:
            await self._set_token(
                url=token.url,
                nonce=token.params.nonce,
                auth=token.params.auth,
                steamid=auth_session.steamid,
            )
        if not self._steamid and tokens.steamID:
            self._steamid = int(tokens.steamID)
        cookies = {
            'steamcommunity.com': self._requests.cookies('steamcommunity.com'),
        }
        for url in ('https://store.steampowered.com', 'https://help.steampowered.com'):
            await self._requests.bytes(url, 'GET')
            cookies.update({
                parse_url(url).host: self._requests.cookies(parse_url(url).host),
            })
        await self._storage.set(login=self._login, cookies=cookies)
