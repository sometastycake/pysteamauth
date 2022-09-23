from typing import (
    Dict,
    Optional,
    Type,
)

from .codes import STEAM_ERROR_CODES


class SteamError(Exception):

    def __init__(self, error_code: int, error_msg: Optional[str] = None):
        self.error_code = error_code
        self.error_msg = error_msg

    def __str__(self) -> str:
        return str({
            'error': STEAM_ERROR_CODES.get(self.error_code, self.error_code),
            'msg': self.error_msg,
            'code': self.error_code,
        })


class UnknownSteamError(SteamError):
    ...


_CUSTOM_ERROR_EXCEPTIONS: Dict[int, Type[SteamError]] = {}


def custom_error_exception(errors: Dict[int, Type[SteamError]]) -> None:
    global _CUSTOM_ERROR_EXCEPTIONS
    if not isinstance(errors, dict):
        raise TypeError('The error argument should be dict')

    for _error, _exception in errors.items():
        if not isinstance(_error, int):
            raise TypeError('Error should be an integer')
        if not isinstance(_exception, type) or not issubclass(_exception, SteamError):
            raise TypeError('Exception should be inherited from SteamError')
        if _error not in STEAM_ERROR_CODES:
            raise TypeError(f'Unknown error code {_error}')
        _CUSTOM_ERROR_EXCEPTIONS[_error] = _exception


class UnauthorizedSteamRequestError(Exception):
    ...


class TooManySteamRequestsError(Exception):
    ...
