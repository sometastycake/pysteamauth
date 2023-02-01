from typing import Dict

from pysteamauth.abstract import CookieStorageAbstract
from pysteamauth.abstract.storage import (
    COOKIE_TYPE,
    COOKIES_TYPE,
)
from pysteamauth.auth.utils import platform_to_str
from pysteamauth.pb.steammessages_auth.steamclient_pb2 import EAuthTokenPlatformType


class BaseCookieStorage(CookieStorageAbstract):

    def __init__(self):
        self._cookies: Dict[str, COOKIES_TYPE] = {}

    def _key(self, key: str, platform: EAuthTokenPlatformType) -> str:
        return '%s_%s' % (key, platform_to_str(platform))

    async def set(self, key: str, platform: EAuthTokenPlatformType, cookies: COOKIES_TYPE) -> None:
        self._cookies[self._key(key, platform)] = cookies

    async def get(self, key: str, platform: EAuthTokenPlatformType, domain: str) -> COOKIE_TYPE:
        cookies = self._cookies.get(self._key(key, platform))
        if not cookies:
            return {}
        return cookies.get(domain, {})
