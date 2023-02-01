from abc import (
    ABC,
    abstractmethod,
)
from typing import Dict

from pysteamauth.pb.steammessages_auth.steamclient_pb2 import EAuthTokenPlatformType


DOMAIN_TYPE = str
COOKIE_TYPE = Dict[str, str]
COOKIES_TYPE = Dict[DOMAIN_TYPE, COOKIE_TYPE]


class CookieStorageAbstract(ABC):

    @abstractmethod
    async def set(self, key: str, platform: EAuthTokenPlatformType, cookies: COOKIES_TYPE) -> None:  # noqa:U100
        ...

    @abstractmethod
    async def get(self, key: str, platform: EAuthTokenPlatformType, domain: str) -> COOKIE_TYPE:  # noqa:U100
        ...
