# Asynchronous python library for Steam authorization using protobuf

[![pypi: package](https://img.shields.io/badge/pypi-2.0.0a2-blue)](https://pypi.org/project/pysteamauth/)
[![Python: versions](
https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)]()


## Install

```bash
pip install pysteamauth
```


## Usage

```python
from pysteamauth.auth import Steam
from pysteamauth.auth.schemas import LoginResult


async def main():
    steam = Steam(
        login='login', 
        password='password',
        steamid=76560000000000000,
    )
    
    result: LoginResult = await steam.login_to_steam()

    response: str = await steam.request(
        url='https://steamcommunity.com',
        method='GET',
    )
```

## If account have Steam Guard

```python
from pysteamauth.auth import Steam

steam = Steam(
    login='login',
    password='password',
    shared_secret='shared_secret',
    steamid=76560000000000000,
)
```

## Cookie storage

Library uses default cookie storage `BaseCookieStorage`, which stores Steam cookies in application memory.
But you can write own cookie storage. For example, redis storage:

```python
import json
from typing import Dict

from aioredis import Redis

from pysteamauth.auth import Steam
from pysteamauth.base import BaseCookieStorage
from pysteamauth.pb.steammessages_auth.steamclient_pb2 import EAuthTokenPlatformType


class RedisStorage(BaseCookieStorage):
    redis = Redis()

    async def set(self, key: str, platform: EAuthTokenPlatformType, cookies: Dict) -> None:
        await self.redis.set(self._key(key, platform), json.dumps(cookies))

    async def get(self, key: str, platform: EAuthTokenPlatformType, domain: str) -> Dict:
        cookies = await self.redis.get(self._key(key, platform))
        if not cookies:
            return {}
        return json.loads(cookies).get(domain, {})


async def main():
    steam = Steam(
        login='login',
        password='password',
        steamid=76560000000000000,
        cookie_storage=RedisStorage(),
    )

    await steam.login_to_steam()
```

## Error processing

```python
from pysteamauth.auth import Steam
from pysteamauth.errors import SteamError


async def main():
    try:
        await Steam('login', 'password', 76560000000000000).login_to_steam()
    except SteamError as error:
        print(error)
```

#### Or

```python
from pysteamauth.auth import Steam
from pysteamauth.errors import SteamError, custom_error_exception


class LoginError(SteamError):
    ...


class RateLimitExceeded(SteamError):
    ...


custom_error_exception({
    5: LoginError,
    84: RateLimitExceeded,
})


async def main():
    try:
        await Steam('login', 'password', 76560000000000000).login_to_steam()
    except LoginError as error:
        print(error)
```

#### Output
`{'error': 'InvalidPassword', 'code': 5}`

## Proto files

- https://github.com/SteamDatabase/Protobufs/blob/master/steam/enums.proto
- https://github.com/SteamDatabase/Protobufs/blob/master/steam/steammessages_base.proto
- https://github.com/SteamDatabase/Protobufs/blob/master/steam/steammessages_auth.steamclient.proto
- https://github.com/SteamDatabase/Protobufs/blob/master/steam/steammessages_unified_base.steamclient.proto

## License

MIT