from typing import Dict

from pysteamauth.abstract import CookieStorageAbstract
from pysteamauth.auth.helpers import platform_to_str
from pysteamauth.pb.steammessages_auth.steamclient_pb2 import EAuthTokenPlatformType as PlatformType


class BaseCookieStorage(CookieStorageAbstract):

    def __init__(self):
        self._cookies: Dict[str, Dict[str, Dict[str, str]]] = {}

    def _key(self, key: str, platform: PlatformType) -> str:
        return '%s_%s' % (key, platform_to_str(platform))

    async def set(self, key: str, platform: PlatformType, cookies: Dict[str, Dict[str, str]]) -> None:
        self._cookies[self._key(key, platform)] = cookies

    async def get(self, key: str, platform: PlatformType, domain: str) -> Dict[str, str]:
        cookies = self._cookies.get(self._key(key, platform))
        if not cookies:
            return {}
        return cookies.get(domain, {})
