from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Any,
    Dict,
    Union,
)


class RequestStrategyAbstract(ABC):

    @abstractmethod
    async def request(self, url: str, method: str, in_bytes: bool = False, **kwargs: Any) -> Union[str, bytes]:
        ...

    async def get_cookies(self, url: str, method: str, **kwargs: Any) -> Dict[str, str]:
        ...
