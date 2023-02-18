import asyncio
import json
from typing import (
    Any,
    Dict,
    List,
    Optional,
)

import aiohttp
from aiohttp import (
    ClientResponse,
    FormData,
)
from yarl import URL

from pysteamauth.abstract import (
    CookieStorageAbstract,
    RequestStrategyAbstract,
)
from pysteamauth.auth.helpers import pbmessage_to_request
from pysteamauth.auth.schemas import (
    FinalizeLoginStatus,
    TransferInfoItem,
)
from pysteamauth.base import (
    BaseCookieStorage,
    BaseRequestStrategy,
)
from pysteamauth.pb.steammessages_auth.steamclient_pb2 import (
    CAuthentication_AccessToken_GenerateForApp_Request,
    CAuthentication_AccessToken_GenerateForApp_Response,
    CAuthentication_PollAuthSessionStatus_Request,
    CAuthentication_PollAuthSessionStatus_Response,
)


class BaseSteam:

    def __init__(
            self,
            request_strategy: Optional[RequestStrategyAbstract] = None,
            cookie_storage: Optional[CookieStorageAbstract] = None,
    ):
        if isinstance(request_strategy, RequestStrategyAbstract):
            self._requests = request_strategy
        elif request_strategy is None:
            self._requests = BaseRequestStrategy(
                raise_for_status=True,
                timeout=aiohttp.ClientTimeout(total=30),
            )
        else:
            raise TypeError('Requests strategy is not realizing RequestStrategyAbstract')

        if isinstance(cookie_storage, CookieStorageAbstract):
            self._storage = cookie_storage
        elif cookie_storage is None:
            self._storage = BaseCookieStorage()
        else:
            raise TypeError('Cookie storage is not realizing CookieStorageAbstract')

    async def cookies(self, domain: str = 'steamcommunity.com') -> Dict[str, str]:
        raise NotImplementedError

    async def sessionid(self, domain: str = 'steamcommunity.com') -> str:
        return (await self.cookies(domain))['sessionid']

    async def request(self, url: str, method: str = 'GET', **kwargs: Any) -> str:
        cookies = await self.cookies(
            domain=URL(url).raw_host,
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

    async def is_alive_session(self) -> bool:
        response: str = await self.request(
            url='https://steamcommunity.com/chat/clientjstoken',
        )
        return json.loads(response)['logged_in']

    async def _poll_auth_session_status(
            self,
            client_id: int,
            request_id: bytes,
    ) -> CAuthentication_PollAuthSessionStatus_Response:
        message = CAuthentication_PollAuthSessionStatus_Request(
            client_id=client_id,
            request_id=request_id,
        )
        response = await self._requests.bytes(
            method='POST',
            url='https://api.steampowered.com/IAuthenticationService/PollAuthSessionStatus/v1',
            data=FormData(
                fields=[
                    ('input_protobuf_encoded', pbmessage_to_request(message)),
                ],
            ),
        )
        return CAuthentication_PollAuthSessionStatus_Response.FromString(response)

    async def _finalize_login(self, refresh_token: str, sessionid: str) -> FinalizeLoginStatus:
        response = await self._requests.text(
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

    async def _set_tokens(self, steamid: int, transfer_info: List[TransferInfoItem]) -> None:
        tasks = []
        for token in transfer_info:
            tasks.append(
                self._set_token(
                    url=token.url,
                    nonce=token.params.nonce,
                    auth=token.params.auth,
                    steamid=steamid,
                )
            )
        await asyncio.gather(*tasks)

    async def _set_token(self, url: str, nonce: str, auth: str, steamid: int) -> ClientResponse:
        form = FormData()
        form.add_field('nonce', nonce)
        form.add_field('auth', auth)
        form.add_field('steamID', str(steamid))
        return await self._requests.request(url, 'POST', data=form)

    async def enumerate_tokens(self, access_key: str) -> Dict:
        response = await self._requests.text(
            method='POST',
            url='https://api.steampowered.com/IAuthenticationService/EnumerateTokens/v1',
            params={
                'access_token': access_key,
            },
        )
        return json.loads(response)

    async def refresh_access_token(
            self,
            steamid: int,
            access_token: str,
            refresh_token: str,
    ) -> CAuthentication_AccessToken_GenerateForApp_Response:
        message = CAuthentication_AccessToken_GenerateForApp_Request(
            steamid=steamid,
            refresh_token=refresh_token,
        )
        response = await self._requests.bytes(
            method='POST',
            url='https://api.steampowered.com/IAuthenticationService/GenerateAccessTokenForApp/v1',
            params={
                'access_token': access_token,
            },
            data=FormData(
                fields=[
                    ('input_protobuf_encoded', pbmessage_to_request(message)),
                ],
            ),
        )
        return CAuthentication_AccessToken_GenerateForApp_Response.FromString(response)
