# Asynchronous python library for Steam authorization using protobuf


## Usage

```
steam = Steam('login', 'password')

# Authorization
await steam.login_to_steam()

# Check authorization
result: bool = await steam.is_authorized()

await steam.request('https://steamcommunity.com')
await steam.request('https://store.steampowered.com')
await steam.request('https://help.steampowered.com')

# If account have Steam Guard
steam = Steam(
    login='login',
    password='password',
    authenticator=AuthenticatorData(
        shared_secret='shared_secret',
    ),
)
```

## Cookie storage

Library uses default cookie storage `BaseCookieStorage`, which stores Steam cookies in application memory.
But you can write own cookie storage. For example, redis storage:

```
class RedisCookieStorage(CookieStorageAbstract):

    redis = Redis()

    async def set(self, login: str, cookies: Dict[str, Any]) -> None:
        await self.redis.set(login, json.dumps(cookies))

    async def get(self, login: str, domain='steamcommunity.com') -> Dict[str, Any]:
        cookies = await self.redis.get(login)
        if not cookies:
            return {}
        return json.loads(cookies).get(domain, {})


steam = Steam(
    login='login',
    password='password',
    cookie_storage=RedisCookieStorage
)
```