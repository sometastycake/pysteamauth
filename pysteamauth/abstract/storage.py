from abc import (
    ABC,
    abstractmethod,
)
from typing import Mapping


COOKIES_TYPE = Mapping[str, Mapping[str, str]]
COOKIES_DOMAIN_TYPE = Mapping[str, str]


class CookieStorageAbstract(ABC):

    @abstractmethod
    async def set(self, login: str, cookies: COOKIES_TYPE) -> None:
        ...

    @abstractmethod
    async def get(self, login: str, domain: str = 'steamcommunity.com') -> COOKIES_DOMAIN_TYPE:
        ...
