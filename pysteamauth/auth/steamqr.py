import asyncio
import base64
import hashlib
import hmac
from typing import (
    Dict,
    List,
    Optional,
)

from aiohttp import FormData
from urllib3.util import parse_url
from yarl import URL

from pysteamauth.abstract import (
    CookieStorageAbstract,
    RequestStrategyAbstract,
)
from pysteamauth.auth.schemas import LoginResult
from pysteamauth.auth.steambase import BaseSteam
from pysteamauth.auth.utils import pbmessage_to_request
from pysteamauth.pb.enums_pb2 import (
    ESessionPersistence,
    k_ESessionPersistence_Persistent,
)
from pysteamauth.pb.steammessages_auth.steamclient_pb2 import (
    CAuthentication_BeginAuthSessionViaQR_Request,
    CAuthentication_BeginAuthSessionViaQR_Response,
    CAuthentication_UpdateAuthSessionWithMobileConfirmation_Request,
    CAuthentication_UpdateAuthSessionWithMobileConfirmation_Response,
    k_EAuthTokenPlatformType_WebBrowser,
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

    async def cookies(self, domain: str = 'steamcommunity.com') -> Dict[str, str]:
        return await self._storage.get(
            key=self._steamid,
            domain=domain,
            platform=k_EAuthTokenPlatformType_WebBrowser,
        )

    async def _begin_auth_session_via_qr(self) -> CAuthentication_BeginAuthSessionViaQR_Response:
        message = CAuthentication_BeginAuthSessionViaQR_Request(
            platform_type=k_EAuthTokenPlatformType_WebBrowser
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

    def _create_auth_session_signature(self, client_id: int, version: int) -> hmac.HMAC:
        message = (
            version.to_bytes(2, 'little') +
            client_id.to_bytes(8, 'little') +
            self._steamid.to_bytes(8, 'little')
        )
        return hmac.new(
            key=base64.b64decode(self._shared_secret),
            msg=message,
            digestmod=hashlib.sha256,
        )

    async def _update_auth_session_with_mobile_confirmation(
            self,
            client_id: int,
            version: int,
            persistence: ESessionPersistence,
    ) -> CAuthentication_UpdateAuthSessionWithMobileConfirmation_Response:
        signature = self._create_auth_session_signature(
            client_id=client_id,
            version=version
        )
        message = CAuthentication_UpdateAuthSessionWithMobileConfirmation_Request(
            client_id=client_id,
            version=version,
            steamid=self._steamid,
            confirm=True,
            signature=signature.digest(),
            persistence=persistence,
        )
        response = await self._requests.bytes(
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
        return CAuthentication_UpdateAuthSessionWithMobileConfirmation_Response.FromString(response)

    async def _set_additional_cookies(self, urls: List[str]) -> None:
        tasks = []
        for url in urls:
            tasks.append(
                self._requests.request(
                    url=URL(url).origin(),
                    method='GET',
                )
            )
        await asyncio.gather(*tasks)

    async def login_to_steam(
            self,
            persistence: ESessionPersistence = k_ESessionPersistence_Persistent,
    ) -> Optional[LoginResult]:
        if await self.is_alive_session():
            return None
        await self._requests.request(
            url='https://steamcommunity.com/',
            method='GET',
        )
        session = await self._begin_auth_session_via_qr()
        await self._update_auth_session_with_mobile_confirmation(
            client_id=session.client_id,
            version=session.version,
            persistence=persistence,
        )
        session_status = await self._poll_auth_session_status(
            client_id=session.client_id,
            request_id=session.request_id,
        )
        sessionid = self._requests.cookies()['sessionid']
        tokens = await self._finalize_login(
            refresh_token=session_status.refresh_token,
            sessionid=sessionid,
        )
        urls = [token.url for token in tokens.transfer_info]
        await self._set_tokens(self._steamid, tokens.transfer_info)
        await self._set_additional_cookies(urls)
        cookies = {}
        for url in urls:
            host = parse_url(url).host
            cookies.update({
                host: self._requests.cookies(host),
            })
        await self._storage.set(
            key=str(self.steamid),
            platform=k_EAuthTokenPlatformType_WebBrowser,
            cookies=cookies,
        )
        return LoginResult(
            client_id=session.client_id,
            refresh_token=session_status.refresh_token,
            access_token=session_status.access_token,
        )
