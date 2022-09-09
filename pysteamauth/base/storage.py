from typing import Dict

from pysteamauth.abstract import (
    COOKIES_DOMAIN_TYPE,
    COOKIES_TYPE,
    CookieStorageAbstract,
)


class BaseCookieStorage(CookieStorageAbstract):

    def __init__(self):
        self.cookies: Dict[str, COOKIES_TYPE] = {}

    async def set(self, login: str, cookies: COOKIES_TYPE) -> None:
        self.cookies[login] = cookies

    async def get(self, login: str, domain: str = 'steamcommunity.com') -> COOKIES_DOMAIN_TYPE:
        cookies = self.cookies.get(login)
        if not cookies:
            return {}
        return cookies.get(domain, {})
