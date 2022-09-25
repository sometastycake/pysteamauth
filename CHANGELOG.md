# Pysteamauth changelog

## [v0.0.5 (2022-09-25)](https://github.com/sometastycake/pysteamauth/releases/tag/v0.0.5)

- Updated protobuf version

## [v0.0.4 (2022-09-25)](https://github.com/sometastycake/pysteamauth/releases/tag/v0.0.4)

- Reduced versions of dependencies

## [v0.0.3 (2022-09-25)](https://github.com/sometastycake/pysteamauth/releases/tag/v0.0.3)

- Use method _bytes_ for Steam requests

## [v0.0.2 (2022-09-24)](https://github.com/sometastycake/pysteamauth/releases/tag/v0.0.2)

- New method _get_confirmation_hash_
- Ability to define custom exceptions for various http status codes from Steam
- Removed method of cookie cleaning from cookie storage
- Method _check_steam_error_ now get _error_msg_ parameter
- New exceptions _UnauthorizedSteamRequestError_ and _TooManySteamRequestsError_
- Steam class get _steamid_ parameter
- New method to get Steam sessionid
- Methods to get steamid and authenticator data

## [v0.0.1 (2022-09-14)](https://github.com/sometastycake/pysteamauth/releases/tag/v0.0.1)

- Steam authorization using protobuf
- Steam error handling
- Requests with Steam session
- Ability to define custom exceptions
