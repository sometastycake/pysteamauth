# Pysteamauth changelog

## [v0.0.7 (2022-10-02)](https://github.com/sometastycake/pysteamauth/releases/tag/v0.0.7)

- Removed exceptions **UnauthorizedSteamRequestError** and **TooManySteamRequestsError**

## [v0.0.6 (2022-09-28)](https://github.com/sometastycake/pysteamauth/releases/tag/v0.0.6)

- Fixed **check_http_status** method

## [v0.0.5 (2022-09-25)](https://github.com/sometastycake/pysteamauth/releases/tag/v0.0.5)

- Updated protobuf version

## [v0.0.4 (2022-09-25)](https://github.com/sometastycake/pysteamauth/releases/tag/v0.0.4)

- Reduced versions of dependencies

## [v0.0.3 (2022-09-25)](https://github.com/sometastycake/pysteamauth/releases/tag/v0.0.3)

- Use method **bytes** for Steam requests

## [v0.0.2 (2022-09-24)](https://github.com/sometastycake/pysteamauth/releases/tag/v0.0.2)

- New method **get_confirmation_hash**
- Ability to define custom exceptions for various http status codes from Steam
- Removed method of cookie cleaning from cookie storage
- Method **check_steam_error** now get **error_msg** parameter
- New exceptions **UnauthorizedSteamRequestError** and **TooManySteamRequestsError**
- Steam class get **steamid** parameter
- New method to get Steam sessionid
- Methods to get steamid and authenticator data

## [v0.0.1 (2022-09-14)](https://github.com/sometastycake/pysteamauth/releases/tag/v0.0.1)

- Steam authorization using protobuf
- Steam error handling
- Requests with Steam session
- Ability to define custom exceptions
