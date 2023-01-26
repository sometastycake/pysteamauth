from typing import Dict

from pysteamauth.abstract import CookieStorageAbstract


class BaseCookieStorage(CookieStorageAbstract):

    def __init__(self):
        self.cookies: Dict[str, Dict[str, Dict[str, str]]] = {}

    async def set(self, key: str, cookies: Dict[str, Dict[str, str]]) -> None:
        self.cookies[key] = cookies

    async def get(self, key: str, domain: str) -> Dict[str, str]:
        cookies = self.cookies.get(key)
        if not cookies:
            return {}
        return cookies.get(domain, {})
