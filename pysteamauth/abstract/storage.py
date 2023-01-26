from abc import (
    ABC,
    abstractmethod,
)
from typing import Mapping


class CookieStorageAbstract(ABC):

    @abstractmethod
    async def set(self, key: str, cookies: Mapping[str, Mapping[str, str]]) -> None:  # noqa:U100
        ...

    @abstractmethod
    async def get(self, key: str, domain: str) -> Mapping[str, str]:  # noqa:U100
        ...
