from typing import (
    Dict,
    Mapping,
)

from pysteamauth.abstract import CookieStorageAbstract


class BaseCookieStorage(CookieStorageAbstract):

    def __init__(self):
        self.cookies: Dict[str, Mapping[str, Mapping[str, str]]] = {}

    async def set(self, key: str, cookies: Mapping[str, Mapping[str, str]]) -> None:
        self.cookies[key] = cookies

    async def get(self, key: str, domain: str) -> Mapping[str, str]:
        cookies = self.cookies.get(key)
        if not cookies:
            return {}
        return cookies.get(domain, {})
