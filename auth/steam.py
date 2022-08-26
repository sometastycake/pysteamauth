import base64
import binascii
import hashlib
import hmac
import math
from struct import pack
from typing import (
    Any,
    Dict,
    Optional,
    Type,
    TypeVar,
)

import aiohttp
import rsa
from aiohttp import FormData
from yarl import URL

from auth.exceptions import LoginError
from auth.schemas import (
    AuthenticatorData,
    FinalizeLoginStatus,
)
from auth.storage import (
    CookieStorage,
    RedisStorage,
)
from pb2_schemas.enums_pb2 import k_ESessionPersistence_Persistent
from pb2_schemas.steammessages_auth.steamclient_pb2 import (
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


StorageType = TypeVar('StorageType', bound=CookieStorage)


class SteamAuth:

    steam_guard_codes = [
        50, 51, 52, 53, 54, 55, 56, 57, 66, 67, 68, 70, 71,
        72, 74, 75, 77, 78, 80, 81, 82, 84, 86, 87, 88, 89,
    ]

    def __init__(
        self,
        login: str,
        password: str,
        authenticator: AuthenticatorData,
        storage: Type[StorageType] = RedisStorage,
    ):
        self._session: Optional[aiohttp.ClientSession] = None
        self.login = login
        self.password = password
        self.authenticator = authenticator
        self.storage = storage()

    @property
    def session(self) -> aiohttp.ClientSession:
        if self._session is None:
            self._session = aiohttp.ClientSession(
                connector=aiohttp.TCPConnector(ssl=False),
                raise_for_status=True,
                cookie_jar=aiohttp.DummyCookieJar(),
            )
        return self._session

    def __del__(self):
        if self._session:
            self._session.connector.close()

    async def request(
        self,
        url: str,
        method: str = 'GET',
        cookie_domain: str = 'steamcommunity.com',
        is_json: bool = False,
        **kwargs: Any
    ) -> Any:
        """
        Request with Steam session.
        Cookie domain may be (store.steampowered.com | help.steampowered.com | steamcommunity.com).
        """
        cookies = await self.storage.get(self.login, cookie_domain)
        response = await self.session.request(
            url=url,
            method=method,
            cookies=cookies,
            **kwargs,
        )
        if is_json:
            return await response.json()
        return await response.text()

    async def is_authorized(self) -> bool:
        """
        Is alive authorization.
        """
        response: Dict = await self.request(
            url='https://steamcommunity.com/chat/clientjstoken',
            is_json=True
        )
        return response['logged_in']

    async def get_sessionid_from_steam(self) -> str:
        """
        Get sessionid cookie.
        """
        response = await self.session.get(
            url='https://steamcommunity.com',
        )
        return response.cookies.get('sessionid').value

    async def getrsakey(self) -> CAuthentication_GetPasswordRSAPublicKey_Response:
        """
        Get rsa keys for password encryption.
        """
        message = CAuthentication_GetPasswordRSAPublicKey_Request(
            account_name=self.login,
        )
        response = await self.session.get(
            url='https://api.steampowered.com/IAuthenticationService/GetPasswordRSAPublicKey/v1',
            params={
                'input_protobuf_encoded': str(base64.b64encode(message.SerializeToString()), 'utf8'),
            },
        )
        data = await response.content.read()
        return CAuthentication_GetPasswordRSAPublicKey_Response.FromString(data)

    async def begin_auth_session(
            self,
            encrypted_password: str,
            rsa_timestamp: int,
    ) -> CAuthentication_BeginAuthSessionViaCredentials_Response:
        """
        Begin auth session.
        """
        user_agent = (
            'Mozilla/5.0 (Linux; Android 2.3) AppleWebKit/535.2 '
            '(KHTML, like Gecko) Chrome/20.0.850.0 Safari/535.2'
        )
        message = CAuthentication_BeginAuthSessionViaCredentials_Request(
            account_name=self.login,
            encrypted_password=encrypted_password,
            encryption_timestamp=rsa_timestamp,
            remember_login=True,
            platform_type=k_EAuthTokenPlatformType_WebBrowser,
            website_id='Community',
            persistence=k_ESessionPersistence_Persistent,
            device_friendly_name=user_agent,
        )
        response = await self.session.post(
            url='https://api.steampowered.com/IAuthenticationService/BeginAuthSessionViaCredentials/v1',
            data=FormData(
                fields=[
                    ('input_protobuf_encoded', str(base64.b64encode(message.SerializeToString()), 'utf8'))
                ]
            ),
        )
        data = await response.content.read()
        return CAuthentication_BeginAuthSessionViaCredentials_Response.FromString(data)

    async def get_server_time(self) -> int:
        """
        Get server time.
        """
        response = await self.session.post(
            url='https://api.steampowered.com/ITwoFactorService/QueryTime/v0001',
        )
        data = await response.json()
        return int(data['response']['server_time'])

    async def get_steam_guard(self) -> str:
        """
        Calculating Steam Guard code.
        """
        server_time = await self.get_server_time()

        data = binascii.unhexlify(
            hmac.new(
                key=base64.b64decode(self.authenticator.shared_secret),
                msg=pack('!L', 0) + pack('!L', math.floor(server_time // 30)),
                digestmod=hashlib.sha1,
            ).hexdigest(),
        )

        value = data[19] & 0xF
        code_point = (
            (data[value] & 0x7F) << 24 |       # noqa:W504
            (data[value + 1] & 0xFF) << 16 |   # noqa:W504
            (data[value + 2] & 0xFF) << 8 |    # noqa:W504
            (data[value + 3] & 0xFF)
        )

        code = ''
        for _ in range(5):
            code += chr(self.steam_guard_codes[code_point % len(self.steam_guard_codes)])
            code_point //= len(self.steam_guard_codes)

        return code

    def encrypt_password(self, keys: CAuthentication_GetPasswordRSAPublicKey_Response) -> str:
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
            message=self.password.encode('ascii'),
            pub_key=public_key,
        )
        return str(base64.b64encode(encrypted_password), 'utf8')

    async def update_auth_session(
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
        await self.session.post(
            url='https://api.steampowered.com/IAuthenticationService/UpdateAuthSessionWithSteamGuardCode/v1',
            data=FormData(
                fields=[
                    ('input_protobuf_encoded', str(base64.b64encode(message.SerializeToString()), 'utf8'))
                ]
            ),
        )

    async def poll_auth_session_status(
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
        response = await self.session.post(
            url='https://api.steampowered.com/IAuthenticationService/PollAuthSessionStatus/v1',
            data=FormData(
                fields=[
                    ('input_protobuf_encoded', str(base64.b64encode(message.SerializeToString()), 'utf8'))
                ]
            ),
        )
        data = await response.content.read()
        return CAuthentication_PollAuthSessionStatus_Response.FromString(data)

    async def finalize_login(self, refresh_token: str, sessionid: str) -> FinalizeLoginStatus:
        """
        Finalize login.
        """
        response = await self.session.post(
            url='https://login.steampowered.com/jwt/finalizelogin',
            data=FormData(
                fields=[
                    ('nonce', refresh_token),
                    ('sessionid', sessionid),
                    ('redir', 'https://steamcommunity.com/login/home/?goto='),
                ],
            ),
        )
        return FinalizeLoginStatus.parse_raw(await response.text())

    async def set_token(self, url: str, nonce: str, auth: str, steamid: int) -> str:
        """
        Set token.

        :return: SteamLoginSecure cookie value.
        """
        response = await self.session.post(
            url=url,
            data=FormData(
                fields=[
                    ('nonce', nonce),
                    ('auth', auth),
                    ('steamID', str(steamid)),
                ],
            ),
        )
        return response.cookies.get('steamLoginSecure').value

    async def login_to_steam(self) -> None:
        """
        Login to Steam.
        """
        if await self.is_authorized():
            return
        sessionid = await self.get_sessionid_from_steam()
        keys = await self.getrsakey()
        encrypted_password = self.encrypt_password(keys)
        auth_session = await self.begin_auth_session(
            encrypted_password=encrypted_password,
            rsa_timestamp=keys.timestamp,
        )
        if not auth_session.steamid:
            raise LoginError(f'Login error "{self.login}"')
        if auth_session.allowed_confirmations:
            if auth_session.allowed_confirmations[0].confirmation_type == k_EAuthSessionGuardType_DeviceCode:
                code = await self.get_steam_guard()
                await self.update_auth_session(
                    client_id=auth_session.client_id,
                    steamid=auth_session.steamid,
                    code=code,
                    code_type=k_EAuthSessionGuardType_DeviceCode,
                )
        auth_session_status = await self.poll_auth_session_status(
            client_id=auth_session.client_id,
            request_id=auth_session.request_id,
        )
        cookies = {}
        transfer_info_response = await self.finalize_login(
            refresh_token=auth_session_status.refresh_token,
            sessionid=sessionid,
        )
        for tranfer in transfer_info_response.transfer_info:
            steam_login_secure = await self.set_token(
                url=tranfer.url,
                nonce=tranfer.params.nonce,
                auth=tranfer.params.auth,
                steamid=auth_session.steamid,
            )
            host = URL(tranfer.url).host
            cookies[host] = {
                'sessionid': sessionid,
                'steamLoginSecure': steam_login_secure,
                'Steam_Language': 'english',
            }
        await self.storage.set(login=self.login, cookies=cookies)
