from abc import (
    ABC,
    abstractmethod,
)
from typing import Dict


class CookieStorageAbstract(ABC):

    @abstractmethod
    async def set(self, key: str, cookies: Dict[str, Dict[str, str]]) -> None:  # noqa:U100
        ...

    @abstractmethod
    async def get(self, key: str, domain: str) -> Dict[str, str]:  # noqa:U100
        ...
