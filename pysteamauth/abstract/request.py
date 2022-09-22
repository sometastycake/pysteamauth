from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Any,
    Dict,
    Mapping,
    Type,
)

from aiohttp import ClientResponse


class RequestStrategyAbstract(ABC):

    http_status_exception: Dict[int, Type[Exception]] = {}

    @abstractmethod
    async def request(self, url: str, method: str, **kwargs: Any) -> ClientResponse:  # noqa:U100
        ...

    @abstractmethod
    async def text(self, url: str, method: str, **kwargs: Any) -> str:  # noqa:U100
        ...

    @abstractmethod
    async def bytes(self, url: str, method: str, **kwargs: Any) -> bytes:  # noqa:U100
        ...

    @abstractmethod
    def cookies(self, domain: str = 'steamcommunity.com') -> Mapping[str, str]:  # noqa:U100
        ...
