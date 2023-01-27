from typing import Dict

from pysteamauth.abstract import CookieStorageAbstract
from pysteamauth.abstract.storage import (
    COOKIE_TYPE,
    COOKIES_TYPE,
)


class BaseCookieStorage(CookieStorageAbstract):

    def __init__(self):
        self.cookies: Dict[str, COOKIES_TYPE] = {}

    async def set(self, key: str, cookies: COOKIES_TYPE) -> None:
        self.cookies[key] = cookies

    async def get(self, key: str, domain: str) -> COOKIE_TYPE:
        cookies = self.cookies.get(key)
        if not cookies:
            return {}
        return cookies.get(domain, {})
