from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Any,
    Mapping,
)

from aiohttp import ClientResponse


class RequestStrategyAbstract(ABC):

    @abstractmethod
    async def request(self, url: str, method: str, **kwargs: Any) -> ClientResponse:
        ...

    @abstractmethod
    async def text(self, url: str, method: str, **kwargs: Any) -> str:
        ...

    @abstractmethod
    async def bytes(self, url: str, method: str, **kwargs: Any) -> bytes:
        ...

    @abstractmethod
    def cookies(self, domain: str = 'steamcommunity.com') -> Mapping[str, str]:
        ...
