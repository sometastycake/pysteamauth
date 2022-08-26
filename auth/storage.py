from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Any,
    Dict,
)

from cachetools import TTLCache

from auth.redis import DictRedis


class CookieStorage(ABC):
    """
    Cookie storage abstract.
    """
    @abstractmethod
    async def set(self, login: str, value: Dict) -> None:
        ...

    @abstractmethod
    async def get(self, login: str, domain: str = 'steamcommunity.com') -> Dict:
        ...


class RedisStorage(CookieStorage):

    redis = DictRedis()

    def __init__(self):
        self.cache = TTLCache(maxsize=100, ttl=60)

    async def set(self, login: str, cookies: Dict[str, Any]) -> None:
        await self.redis.set_json(login, cookies)
        self.cache.update({
            login: cookies,
        })

    async def get(self, login: str, domain='steamcommunity.com') -> Dict[str, Any]:
        if self.cache.get(login):
            cookies = self.cache.get(login, {})
            return cookies.get(domain, {})
        cookies = await self.redis.get_json(login, default={})
        self.cache.update({
            login: cookies,
        })
        return cookies.get(domain, {})
