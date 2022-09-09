from .codes import STEAM_ERROR_CODES
from .exceptions import (
    _CUSTOM_ERROR_EXCEPTIONS,
    SteamError,
    UnknownSteamError,
)


def check_steam_error(error: int) -> None:
    if error in (1, 22):
        return
    if error in _CUSTOM_ERROR_EXCEPTIONS:
        raise _CUSTOM_ERROR_EXCEPTIONS[error](error)
    if error in STEAM_ERROR_CODES:
        raise SteamError(error_code=error)
    raise UnknownSteamError(error_code=error)
