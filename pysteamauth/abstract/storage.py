from abc import (
    ABC,
    abstractmethod,
)
from typing import Mapping


class CookieStorageAbstract(ABC):

    @abstractmethod
    async def set(self, login: str, cookies: Mapping[str, Mapping[str, str]]) -> None:  # noqa:U100
        ...

    @abstractmethod
    async def get(self, login: str, domain: str = 'steamcommunity.com') -> Mapping[str, str]:  # noqa:U100
        ...
