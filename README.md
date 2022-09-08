# Asynchronous python library for Steam authorization using protobuf


## Usage

```python
import asyncio

from pysteamauth.auth import Steam


async def main():
    steam = Steam('login', 'password')
    
    await steam.login_to_steam()

    result: bool = await steam.is_authorized()

    await steam.request('https://steamcommunity.com')
    await steam.request('https://store.steampowered.com')
    await steam.request('https://help.steampowered.com')


if __name__ == '__main__':
    asyncio.run(main())
```

## Cookie storage

Library uses default cookie storage `BaseCookieStorage`, which stores Steam cookies in application memory.
But you can write own cookie storage. For example, redis storage:

```python
import asyncio
import json
from typing import Dict

from aioredis import Redis
from pysteamauth.abstract import CookieStorageAbstract
from pysteamauth.auth import Steam


class RedisStorage(CookieStorageAbstract):

    redis = Redis()

    async def set(self, login: str, cookies: Dict) -> None:
        await self.redis.set(login, json.dumps(cookies))

    async def get(self, login: str, domain: str = 'steamcommunity.com') -> Dict:
        cookies = await self.redis.get(login)
        if not cookies:
            return {}
        return json.loads(cookies).get(domain, {})


async def main():
    steam = Steam(
        login='login',
        password='password',
        cookie_storage=RedisStorage,
    )
    
    await steam.login_to_steam()


if __name__ == '__main__':
    asyncio.run(main())

```

## Proto files

- https://github.com/SteamDatabase/Protobufs/blob/master/steam/enums.proto
- https://github.com/SteamDatabase/Protobufs/blob/master/steam/steammessages_base.proto
- https://github.com/SteamDatabase/Protobufs/blob/master/steam/steammessages_auth.steamclient.proto
- https://github.com/SteamDatabase/Protobufs/blob/master/steam/steammessages_unified_base.steamclient.proto
