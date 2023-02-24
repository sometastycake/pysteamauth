from abc import (
    ABC,
    abstractmethod,
)
from typing import Dict

from pysteamauth.pb.steammessages_auth.steamclient_pb2 import EAuthTokenPlatformType as PlatformType


class CookieStorageAbstract(ABC):

    @abstractmethod
    async def set(self, key: str, platform: PlatformType, cookies: Dict[str, Dict[str, str]]) -> None:
        ...

    @abstractmethod
    async def get(self, key: str, platform: PlatformType, domain: str) -> Dict[str, str]:
        ...
