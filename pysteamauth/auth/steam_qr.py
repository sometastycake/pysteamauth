import asyncio
import base64
import hashlib
import hmac
import json
from typing import (
    Any,
    Optional,
)

from aiohttp import FormData
from urllib3.util import parse_url

from pysteamauth.abstract import (
    CookieStorageAbstract,
    RequestStrategyAbstract,
)
from pysteamauth.auth.base_steam import BaseSteam
from pysteamauth.auth.schemas import LoginResult
from pysteamauth.auth.steam import pbmessage_to_request
from pysteamauth.pb.enums_pb2 import ESessionPersistence
from pysteamauth.pb.steammessages_auth.steamclient_pb2 import (
    CAuthentication_BeginAuthSessionViaQR_Request,
    CAuthentication_BeginAuthSessionViaQR_Response,
    CAuthentication_GetAuthSessionInfo_Request,
    CAuthentication_GetAuthSessionInfo_Response,
    CAuthentication_UpdateAuthSessionWithMobileConfirmation_Request,
    EAuthTokenPlatformType,
)


class SteamQR(BaseSteam):

    def __init__(
            self,
            steamid: int,
            shared_secret: str,
            mobile_access_token: str,
            request_strategy: Optional[RequestStrategyAbstract] = None,
            cookie_storage: Optional[CookieStorageAbstract] = None,
    ):
        super().__init__(request_strategy, cookie_storage)
        self._steamid = steamid
        self._shared_secret = shared_secret
        self._mobile_access_token = mobile_access_token

    @property
    def steamid(self) -> int:
        return self._steamid

    async def request(self, url: str, method: str = 'GET', **kwargs: Any) -> str:
        cookies = await self._storage.get(
            login=str(self._steamid),
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
        return json.loads(response)['logged_in']

    async def _begin_auth_session(self) -> CAuthentication_BeginAuthSessionViaQR_Response:
        message = CAuthentication_BeginAuthSessionViaQR_Request(
            device_friendly_name=(
                'Mozilla/5.0 (X11; Linux x86_64; rv:1.9.5.20) Gecko/2812-12-10 04:56:28 Firefox/3.8'
            ),
            platform_type=EAuthTokenPlatformType.k_EAuthTokenPlatformType_WebBrowser
        )
        response = await self._requests.bytes(
            method='POST',
            url='https://api.steampowered.com/IAuthenticationService/BeginAuthSessionViaQR/v1',
            data=FormData(
                fields=[
                    ('input_protobuf_encoded', pbmessage_to_request(message)),
                ],
            ),
        )
        return CAuthentication_BeginAuthSessionViaQR_Response.FromString(response)

    async def get_session_info(self, client_id: int) -> CAuthentication_GetAuthSessionInfo_Response:
        message = CAuthentication_GetAuthSessionInfo_Request(
            client_id=client_id,
        )
        response = await self._requests.bytes(
            method='POST',
            url='https://api.steampowered.com/IAuthenticationService/GetAuthSessionInfo/v1',
            params={
                'access_token': self._mobile_access_token,
            },
            data=FormData(
                fields=[
                    ('input_protobuf_encoded', pbmessage_to_request(message)),
                ],
            ),
        )
        return CAuthentication_GetAuthSessionInfo_Response.FromString(response)

    async def _update_auth_session(self, client_id: int, version: int) -> None:
        message = version.to_bytes(2, 'little')
        message += client_id.to_bytes(8, 'little')
        message += self.steamid.to_bytes(8, 'little')

        signature = hmac.new(
            key=base64.b64decode(self._shared_secret),
            msg=message,
            digestmod=hashlib.sha256,
        )

        message = CAuthentication_UpdateAuthSessionWithMobileConfirmation_Request(
            client_id=client_id,
            version=version,
            steamid=self._steamid,
            confirm=True,
            signature=signature.digest(),
            persistence=ESessionPersistence.k_ESessionPersistence_Persistent,
        )
        await self._requests.text(
            method='POST',
            url='https://api.steampowered.com/IAuthenticationService/UpdateAuthSessionWithMobileConfirmation/v1',
            params={
                'access_token': self._mobile_access_token,
            },
            data=FormData(
                fields=[
                    ('input_protobuf_encoded', pbmessage_to_request(message)),
                ],
            ),
        )

    async def login_to_steam(self) -> Optional[LoginResult]:
        if await self.is_authorized():
            return None
        await self._requests.request(
            url='https://steamcommunity.com/',
            method='GET',
        )
        authsession = await self._begin_auth_session()
        await self._update_auth_session(
            client_id=authsession.client_id,
            version=authsession.version,
        )
        session_status = await self._poll_auth_session_status(
            client_id=authsession.client_id,
            request_id=authsession.request_id,
        )
        sessionid = self._requests.cookies()['sessionid']
        tokens = await self._finalize_login(
            refresh_token=session_status.refresh_token,
            sessionid=sessionid,
        )
        await asyncio.gather(*[
            self._set_token(
                token.url, token.params.nonce, token.params.auth, self._steamid,
            ) for token in tokens.transfer_info
        ])
        cookies = {}
        for token in tokens.transfer_info:
            host = parse_url(token.url).host
            cookies.update({
                host: self._requests.cookies(host),
            })
        await self._storage.set(str(self.steamid), cookies)
        return LoginResult(
            client_id=authsession.client_id,
            refresh_token=session_status.refresh_token,
            access_token=session_status.access_token,
        )
