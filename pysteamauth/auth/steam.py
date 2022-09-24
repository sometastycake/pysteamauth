import base64
import binascii
import hashlib
import hmac
import math
from struct import pack
from typing import (
    Any,
    Mapping,
    Optional,
    Type,
)

import rsa
from aiohttp import FormData
from bitstring import BitArray

from pysteamauth.abstract import (
    CookieStorageAbstract,
    RequestStrategyAbstract,
)
from pysteamauth.base import (
    BaseCookieStorage,
    BaseRequestStrategy,
)
from pysteamauth.pb2.enums_pb2 import ESessionPersistence
from pysteamauth.pb2.steammessages_auth.steamclient_pb2 import (
    CAuthentication_AllowedConfirmation,
    CAuthentication_BeginAuthSessionViaCredentials_Request,
    CAuthentication_BeginAuthSessionViaCredentials_Response,
    CAuthentication_GetPasswordRSAPublicKey_Request,
    CAuthentication_GetPasswordRSAPublicKey_Response,
    CAuthentication_PollAuthSessionStatus_Request,
    CAuthentication_PollAuthSessionStatus_Response,
    CAuthentication_UpdateAuthSessionWithSteamGuardCode_Request,
    EAuthSessionGuardType,
    EAuthTokenPlatformType,
)

from .schemas import (
    AuthenticatorData,
    FinalizeLoginStatus,
    ServerTimeResponse,
    SteamAuthorizationStatus,
)
from .utils import get_host_from_url


class Steam:

    domains = (
        'steamcommunity.com',
        'store.steampowered.com',
        'help.steampowered.com',
    )

    def __init__(
        self,
        login: str,
        password: str,
        steamid: int,
        authenticator: Optional[AuthenticatorData] = None,
        cookie_storage: Type[CookieStorageAbstract] = BaseCookieStorage,
        request_strategy: Type[RequestStrategyAbstract] = BaseRequestStrategy,
    ):
        self._login = login
        self._steamid = steamid
        self._password = password
        self._authenticator = authenticator
        self._http = request_strategy()
        self._storage = cookie_storage()

    @property
    def steamid(self) -> int:
        return self._steamid

    @property
    def authenticator(self) -> Optional[AuthenticatorData]:
        return self._authenticator

    @property
    def login(self) -> str:
        return self._login

    async def cookies(self, domain: str = 'steamcommunity.com') -> Mapping[str, str]:
        return await self._storage.get(
            login=self._login,
            domain=domain,
        )

    async def sessionid(self, domain: str = 'steamcommunity.com') -> str:
        return (await self.cookies(domain))['sessionid']

    async def request(self, url: str, method: str = 'GET', **kwargs: Any) -> str:
        """
        Request with Steam session.
        """
        domain = get_host_from_url(url)

        if domain not in self.domains:
            raise RuntimeError(f'Wrong domain "{domain}"')

        cookies = await self._storage.get(
            login=self._login,
            domain=domain,
        )

        return await self._http.text(
            url=url,
            method=method,
            cookies={
                **cookies,
                **kwargs.pop('cookies', {}),
            },
            **kwargs,
        )

    async def is_authorized(self) -> bool:
        """
        Is alive authorization.
        """
        response: str = await self.request(
            url='https://steamcommunity.com/chat/clientjstoken',
        )
        return SteamAuthorizationStatus.parse_raw(response).logged_in

    async def _getrsakey(self) -> CAuthentication_GetPasswordRSAPublicKey_Response:
        """
        Get rsa keys for password encryption.
        """
        message = CAuthentication_GetPasswordRSAPublicKey_Request(
            account_name=self._login,
        )
        response = await self._http.bytes(
            method='GET',
            url='https://api.steampowered.com/IAuthenticationService/GetPasswordRSAPublicKey/v1',
            params={
                'input_protobuf_encoded': str(base64.b64encode(message.SerializeToString()), 'utf8'),
            },
        )
        return CAuthentication_GetPasswordRSAPublicKey_Response.FromString(response)

    async def _begin_auth_session(
            self,
            encrypted_password: str,
            rsa_timestamp: int,
    ) -> CAuthentication_BeginAuthSessionViaCredentials_Response:
        """
        Begin auth session.
        """
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
        response = await self._http.bytes(
            method='POST',
            url='https://api.steampowered.com/IAuthenticationService/BeginAuthSessionViaCredentials/v1',
            data=FormData(
                fields=[
                    ('input_protobuf_encoded', str(base64.b64encode(message.SerializeToString()), 'utf8')),
                ],
            ),
        )
        return CAuthentication_BeginAuthSessionViaCredentials_Response.FromString(response)

    async def get_server_time(self) -> int:
        """
        Get server time.
        """
        response = await self._http.text(
            method='POST',
            url='https://api.steampowered.com/ITwoFactorService/QueryTime/v0001',
        )
        return ServerTimeResponse.parse_raw(response).response.server_time

    async def get_steam_guard(self, server_time: int) -> str:
        """
        Calculating Steam Guard code.
        """
        if self._authenticator is None:
            raise RuntimeError('Not found authenticator')

        data = binascii.unhexlify(
            hmac.new(
                key=base64.b64decode(self._authenticator.shared_secret),
                msg=pack('!L', 0) + pack('!L', math.floor(server_time // 30)),
                digestmod=hashlib.sha1,
            ).hexdigest(),
        )

        value = data[19] & 0xF
        full_code = (
            (data[value] & 0x7F) << 24 |       # noqa:W504
            (data[value + 1] & 0xFF) << 16 |   # noqa:W504
            (data[value + 2] & 0xFF) << 8 |    # noqa:W504
            (data[value + 3] & 0xFF)
        )

        code = ''
        chars = '23456789BCDFGHJKMNPQRTVWXY'
        for _ in range(5):
            code += chars[full_code % len(chars)]
            full_code //= len(chars)

        return code

    def get_confirmation_hash(self, server_time: int, tag: str = 'conf') -> str:
        """
        Get mobile confirmation hash.
        """
        if self._authenticator is None:
            raise RuntimeError('Not found authenticator')
        identitysecret = base64.b64decode(
            self._authenticator.identity_secret,
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
        """
        Encrypt password.
        """
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
            code_type: int,
    ) -> None:
        """
        Update session request.
        """
        message = CAuthentication_UpdateAuthSessionWithSteamGuardCode_Request(
            client_id=client_id,
            steamid=steamid,
            code=code,
            code_type=code_type,
        )
        await self._http.request(
            method='POST',
            url='https://api.steampowered.com/IAuthenticationService/UpdateAuthSessionWithSteamGuardCode/v1',
            data=FormData(
                fields=[
                    ('input_protobuf_encoded', str(base64.b64encode(message.SerializeToString()), 'utf8')),
                ],
            ),
        )

    async def _poll_auth_session_status(
            self,
            client_id: int,
            request_id: bytes,
    ) -> CAuthentication_PollAuthSessionStatus_Response:
        """
        Auth session status.
        """
        message = CAuthentication_PollAuthSessionStatus_Request(
            client_id=client_id,
            request_id=request_id,
        )
        response = await self._http.bytes(
            method='POST',
            url='https://api.steampowered.com/IAuthenticationService/PollAuthSessionStatus/v1',
            data=FormData(
                fields=[
                    ('input_protobuf_encoded', str(base64.b64encode(message.SerializeToString()), 'utf8')),
                ],
            ),
        )
        return CAuthentication_PollAuthSessionStatus_Response.FromString(response)

    async def _finalize_login(self, refresh_token: str, sessionid: str) -> FinalizeLoginStatus:
        """
        Finalize login.
        """
        response = await self._http.text(
            method='POST',
            url='https://login.steampowered.com/jwt/finalizelogin',
            data=FormData(
                fields=[
                    ('nonce', refresh_token),
                    ('sessionid', sessionid),
                    ('redir', 'https://steamcommunity.com/login/home/?goto='),
                ],
            ),
        )
        return FinalizeLoginStatus.parse_raw(response)

    async def _set_token(self, url: str, nonce: str, auth: str, steamid: int) -> None:
        """
        Set token.
        """
        await self._http.request(
            method='POST',
            url=url,
            data=FormData(
                fields=[
                    ('nonce', nonce),
                    ('auth', auth),
                    ('steamID', str(steamid)),
                ],
            ),
        )

    def _is_twofactor_required(self, confirmation: CAuthentication_AllowedConfirmation) -> bool:
        """
        Is twofactor required.
        """
        return confirmation.confirmation_type == EAuthSessionGuardType.k_EAuthSessionGuardType_DeviceCode

    async def login_to_steam(self) -> None:
        """
        Login to Steam.
        """
        if await self.is_authorized():
            return
        if not self._http.cookies().get('sessionid'):
            await self._http.bytes(
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
                server_time = await self.get_server_time()
                code = await self.get_steam_guard(server_time)
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
            sessionid=self._http.cookies()['sessionid'],
        )

        for token in tokens.transfer_info:
            await self._set_token(
                url=token.url,
                nonce=token.params.nonce,
                auth=token.params.auth,
                steamid=auth_session.steamid,
            )
        # Needs to get additional cookies through aiohttp session
        for domain in ('store', 'help'):
            await self._http.bytes(
                method='GET',
                url=f'https://{domain}.steampowered.com',
            )
        # Write cookies from aiohttp session
        cookies = {}
        for domain in self.domains:
            cookies[domain] = self._http.cookies(domain)
        # Save cookies to storage
        await self._storage.set(login=self._login, cookies=cookies)
