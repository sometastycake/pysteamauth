from abc import (
    ABC,
    abstractmethod,
)
from typing import Any

from aiohttp import ClientResponse
from aiohttp.abc import AbstractCookieJar
from aiohttp.typedefs import StrOrURL


class RequestStrategyAbstract(ABC):

    @property
    @abstractmethod
    def cookies(self) -> AbstractCookieJar:
        ...

    @abstractmethod
    async def request(self, url: StrOrURL, method: str, **kwargs: Any) -> ClientResponse:
        ...

    @abstractmethod
    async def text(self, url: StrOrURL, method: str, **kwargs: Any) -> str:
        ...

    @abstractmethod
    async def bytes(self, url: StrOrURL, method: str, **kwargs: Any) -> bytes:
        ...
