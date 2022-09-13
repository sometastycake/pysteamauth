from enum import IntEnum
from typing import (
    List,
    Optional,
)

from pysteamauth.pb2.enums_pb2 import ESessionPersistence


class EAuthTokenPlatformType(IntEnum):
    k_EAuthTokenPlatformType_Unknown: int = 0
    k_EAuthTokenPlatformType_SteamClient: int = 1
    k_EAuthTokenPlatformType_WebBrowser: int = 2
    k_EAuthTokenPlatformType_MobileApp: int = 3


class EAuthSessionGuardType(IntEnum):
    k_EAuthSessionGuardType_Unknown: int = 0
    k_EAuthSessionGuardType_None: int = 1
    k_EAuthSessionGuardType_EmailCode: int = 2
    k_EAuthSessionGuardType_DeviceCode: int = 3
    k_EAuthSessionGuardType_DeviceConfirmation: int = 4
    k_EAuthSessionGuardType_EmailConfirmation: int = 5
    k_EAuthSessionGuardType_MachineToken: int = 6


class CAuthentication_UpdateAuthSessionWithSteamGuardCode_Request:

    def __init__(
        self,
        client_id: int,
        steamid: int,
        code: Optional[str],
        code_type: Optional[int],
    ):
        ...

    @staticmethod
    def FromString(message: bytes) -> 'CAuthentication_UpdateAuthSessionWithSteamGuardCode_Request':
        ...

    def SerializeToString(self) -> bytes:
        ...


class CAuthentication_AllowedConfirmation:
    confirmation_type: EAuthSessionGuardType
    associated_message: Optional[str]


class CAuthentication_BeginAuthSessionViaCredentials_Response:
    client_id: int
    request_id: bytes
    interval: Optional[float]
    allowed_confirmations: Optional[List[CAuthentication_AllowedConfirmation]]
    steamid: int
    weak_token: Optional[str]

    @staticmethod
    def FromString(message: bytes) -> 'CAuthentication_BeginAuthSessionViaCredentials_Response':
        ...

    def SerializeToString(self) -> bytes:
        ...



class CAuthentication_GetPasswordRSAPublicKey_Request:

    def __init__(self, account_name: str):
        ...

    @staticmethod
    def FromString(message: bytes) -> 'CAuthentication_GetPasswordRSAPublicKey_Request':
        ...

    def SerializeToString(self) -> bytes:
        ...


class CAuthentication_BeginAuthSessionViaCredentials_Request:

    def __init__(
        self,
        account_name: str,
        encrypted_password: str,
        encryption_timestamp: int,
        device_friendly_name: str,
        website_id: str = 'Unknown',
        remember_login: bool = True,
        platform_type: int = EAuthTokenPlatformType.k_EAuthTokenPlatformType_Unknown,
        persistence: int = ESessionPersistence.k_ESessionPersistence_Persistent,
    ):
        ...

    @staticmethod
    def FromString(message: bytes) -> 'CAuthentication_BeginAuthSessionViaCredentials_Request':
        ...

    def SerializeToString(self) -> bytes:
        ...


class CAuthentication_PollAuthSessionStatus_Request:

    def __init__(self, client_id: int, request_id: bytes, token_to_revoke: Optional[int] = None):
        ...

    def SerializeToString(self) -> bytes:
        ...


class CAuthentication_GetPasswordRSAPublicKey_Response:
    publickey_mod: str
    publickey_exp: str
    timestamp: int

    @staticmethod
    def FromString(message: bytes) -> 'CAuthentication_GetPasswordRSAPublicKey_Response':
        ...

    def SerializeToString(self) -> bytes:
        ...


class CAuthentication_PollAuthSessionStatus_Response:
    new_client_id: Optional[int]
    new_challenge_url: Optional[str]
    refresh_token: str
    access_token: str
    had_remote_interaction: bool
    account_name: str

    @staticmethod
    def FromString(message: bytes) -> 'CAuthentication_PollAuthSessionStatus_Response':
        ...

    def SerializeToString(self) -> bytes:
        ...
