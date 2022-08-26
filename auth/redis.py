import json
from typing import (
    Any,
    Dict,
    Optional,
)

from aioredis import Redis as BaseRedis


class DictRedis(BaseRedis):

    def __init__(self, **kwargs):
        kwargs['decode_responses'] = True
        super().__init__(**kwargs)

    async def set_json(self, key: str, value: Dict, **kwargs) -> bool:
        return await self.set(key, json.dumps(value), **kwargs)

    async def get_json(self, key: str, default: Optional[Any] = None) -> Optional[Any]:
        try:
            value = await self.get(key)
            if value:
                return json.loads(await self.get(key))
        except (ValueError, TypeError):
            pass
        return default
