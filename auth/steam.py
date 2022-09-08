import base64
import binascii
import hashlib
import hmac
import json
import math
from struct import pack
from typing import (
    Any,
    Optional,
    Type,
    TypeVar,
)

import rsa
from aiohttp import FormData

from abstract import (
    CookieStorageAbstract,
    RequestStrategyAbstract,
)
from auth.schemas import (
    AuthenticatorData,
    FinalizeLoginStatus,
    ServerTimeResponse,
)
from auth.utils import _get_host_from_url
from base import (
    BaseCookieStorage,
    BaseRequestStrategy,
)
from pb2 import k_ESessionPersistence_Persistent
from pb2.steammessages_auth.steamclient_pb2 import (
    CAuthentication_AllowedConfirmation,
    CAuthentication_BeginAuthSessionViaCredentials_Request,
    CAuthentication_BeginAuthSessionViaCredentials_Response,
    CAuthentication_GetPasswordRSAPublicKey_Request,
    CAuthentication_GetPasswordRSAPublicKey_Response,
    CAuthentication_PollAuthSessionStatus_Request,
    CAuthentication_PollAuthSessionStatus_Response,
    CAuthentication_UpdateAuthSessionWithSteamGuardCode_Request,
    k_EAuthSessionGuardType_DeviceCode,
    k_EAuthTokenPlatformType_WebBrowser,
)


CookieStorageType = TypeVar('CookieStorageType', bound=CookieStorageAbstract)
RequestStrategyType = TypeVar('RequestStrategyType', bound=RequestStrategyAbstract)


class Steam:

    def __init__(
        self,
        login: str,
        password: str,
        authenticator: Optional[AuthenticatorData] = None,
        cookie_storage: Type[CookieStorageType] = BaseCookieStorage,
        request_strategy: Type[RequestStrategyType] = BaseRequestStrategy,
    ):
        self._login = login
        self._password = password
        self._authenticator = authenticator
        self._http = request_strategy()
        self._storage = cookie_storage()

    async def request(self, url: str, method: str = 'GET', **kwargs: Any) -> str:
        """
        Request with Steam session.
        """
        return await self._http.request(
            url=url,
            method=method,
            cookies=await self._storage.get(
                login=self._login,
                domain=_get_host_from_url(url),
            ),
            **kwargs,
        )

    async def is_authorized(self) -> bool:
        """
        Is alive authorization.
        """
        response: str = await self.request(
            method='GET',
            url='https://steamcommunity.com/chat/clientjstoken',
        )
        return json.loads(response)['logged_in']

    async def _get_sessionid_from_steam(self) -> str:
        """
        Get sessionid cookie.
        """
        cookies = await self._http.get_cookies(
            method='GET',
            url='https://steamcommunity.com',
        )
        return cookies['sessionid']

    async def _getrsakey(self) -> CAuthentication_GetPasswordRSAPublicKey_Response:
        """
        Get rsa keys for password encryption.
        """
        message = CAuthentication_GetPasswordRSAPublicKey_Request(
            account_name=self._login,
        )
        response = await self._http.request(
            method='GET',
            url='https://api.steampowered.com/IAuthenticationService/GetPasswordRSAPublicKey/v1',
            params={
                'input_protobuf_encoded': str(base64.b64encode(message.SerializeToString()), 'utf8'),
            },
            in_bytes=True,
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
            platform_type=k_EAuthTokenPlatformType_WebBrowser,
            website_id='Community',
            persistence=k_ESessionPersistence_Persistent,
            device_friendly_name='Mozilla/5.0 (X11; Linux x86_64; rv:1.9.5.20) Gecko/2812-12-10 04:56:28 Firefox/3.8',
        )
        response = await self._http.request(
            method='POST',
            url='https://api.steampowered.com/IAuthenticationService/BeginAuthSessionViaCredentials/v1',
            data=FormData(
                fields=[
                    ('input_protobuf_encoded', str(base64.b64encode(message.SerializeToString()), 'utf8'))
                ]
            ),
            in_bytes=True,
        )
        return CAuthentication_BeginAuthSessionViaCredentials_Response.FromString(response)

    async def _get_server_time(self) -> int:
        """
        Get server time.
        """
        response = await self._http.request(
            method='POST',
            url='https://api.steampowered.com/ITwoFactorService/QueryTime/v0001',
        )
        return ServerTimeResponse.parse_raw(response).response.server_time

    async def get_steam_guard(self) -> str:
        """
        Calculating Steam Guard code.
        """
        server_time = await self._get_server_time()

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
                    ('input_protobuf_encoded', str(base64.b64encode(message.SerializeToString()), 'utf8'))
                ]
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
        response = await self._http.request(
            method='POST',
            url='https://api.steampowered.com/IAuthenticationService/PollAuthSessionStatus/v1',
            data=FormData(
                fields=[
                    ('input_protobuf_encoded', str(base64.b64encode(message.SerializeToString()), 'utf8'))
                ]
            ),
            in_bytes=True,
        )
        return CAuthentication_PollAuthSessionStatus_Response.FromString(response)

    async def _finalize_login(self, refresh_token: str, sessionid: str) -> FinalizeLoginStatus:
        """
        Finalize login.
        """
        response = await self._http.request(
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

    async def _set_token(self, url: str, nonce: str, auth: str, steamid: int) -> str:
        """
        Set token.

        :return: SteamLoginSecure cookie value.
        """
        cookies = await self._http.get_cookies(
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
        return cookies['steamLoginSecure']

    def is_twofactor_required(self, confirmation: CAuthentication_AllowedConfirmation) -> bool:
        """
        Is twofactor required.
        """
        return confirmation.confirmation_type == k_EAuthSessionGuardType_DeviceCode

    async def login_to_steam(self) -> None:
        """
        Login to Steam.
        """
        if await self.is_authorized():
            return
        sessionid = await self._get_sessionid_from_steam()
        keys = await self._getrsakey()
        encrypted_password = self._encrypt_password(keys)
        auth_session = await self._begin_auth_session(
            encrypted_password=encrypted_password,
            rsa_timestamp=keys.timestamp,
        )
        if auth_session.allowed_confirmations:
            if self.is_twofactor_required(auth_session.allowed_confirmations[0]):
                code = await self.get_steam_guard()
                await self._update_auth_session(
                    client_id=auth_session.client_id,
                    steamid=auth_session.steamid,
                    code=code,
                    code_type=k_EAuthSessionGuardType_DeviceCode,
                )
        session = await self._poll_auth_session_status(
            client_id=auth_session.client_id,
            request_id=auth_session.request_id,
        )
        tokens = await self._finalize_login(
            refresh_token=session.refresh_token,
            sessionid=sessionid,
        )
        cookies = {}
        for token in tokens.transfer_info:
            cookie = await self._set_token(
                url=token.url,
                nonce=token.params.nonce,
                auth=token.params.auth,
                steamid=auth_session.steamid,
            )
            cookies.update({
                _get_host_from_url(token.url): {
                    'sessionid': sessionid,
                    'steamLoginSecure': cookie,
                    'Steam_Language': 'english',
                }
            })
        await self._storage.set(login=self._login, cookies=cookies)
