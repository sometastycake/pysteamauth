from errors import (
    STEAM_ERROR_CODES,
    SteamError,
    UnknownSteamError,
)


def check_steam_error(error: int) -> None:
    if error in (1, 22):
        return
    if error in STEAM_ERROR_CODES:
        raise SteamError(error_code=error)
    raise UnknownSteamError(error_code=error)
