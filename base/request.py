from typing import (
    Any,
    Dict,
    Optional,
    Union,
)

import aiohttp
from aiohttp import (
    ClientResponse,
    ClientSession,
)

from abstract import RequestStrategyAbstract
from errors import check_steam_error


class BaseRequestStrategy(RequestStrategyAbstract):

    def __init__(self):
        self._session: Optional[ClientSession] = None

    def __del__(self):
        if self._session:
            self._session.connector.close()

    def _create_session(self) -> ClientSession:
        """
        Create aiohttp session.
        Aiohttp session saves and stores cookies.
        It writes cookies from responses after each request that specified
        in Set-Cookie header. This is undesirable behavior, so by using DummyCookies we disable
        autosave of cookies within the aiohttp session.

        :return: aiohttp.ClientSession object.
        """
        return ClientSession(
            connector=aiohttp.TCPConnector(ssl=False),
            cookie_jar=aiohttp.DummyCookieJar(),
        )

    async def _request(self, url: str, method: str, **kwargs: Any) -> ClientResponse:
        if self._session is None:
            self._session = self._create_session()
        return await self._session.request(method, url, **kwargs)

    async def request(self, url: str, method: str, in_bytes: bool = False, **kwargs: Any) -> Union[str, bytes]:
        response = await self._request(url, method, **kwargs)
        error = response.headers.get('X-eresult')
        if error:
            check_steam_error(int(error))
        if in_bytes:
            return await response.content.read()
        return await response.text()

    async def get_cookies(self, url: str, method: str, **kwargs: Any) -> Dict[str, str]:
        response = await self._request(url, method, **kwargs)
        error = response.headers.get('X-eresult')
        if error:
            check_steam_error(int(error))
        return {k: v.value for k, v in response.cookies.items()}
