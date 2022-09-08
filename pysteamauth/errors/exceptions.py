from pysteamauth.errors import STEAM_ERROR_CODES


class SteamError(Exception):

    def __init__(self, error_code: int):
        self.error_code = error_code

    def __str__(self) -> str:
        return str({
            'error': STEAM_ERROR_CODES.get(self.error_code, self.error_code),
            'code': self.error_code,
        })


class UnknownSteamError(SteamError):
    ...
