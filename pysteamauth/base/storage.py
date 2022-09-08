from typing import Dict

from pysteamauth.abstract import CookieStorageAbstract


class BaseCookieStorage(CookieStorageAbstract):

    def __init__(self):
        self.cookies: Dict = {}

    async def set(self, login: str, cookies: Dict) -> None:
        self.cookies[login] = cookies

    async def get(self, login: str, domain: str = 'steamcommunity.com') -> Dict:
        cookies = self.cookies.get(login)
        if not cookies:
            return {}
        return cookies.get(domain, {})
