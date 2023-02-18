from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import List
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

import pysteamauth.pb.enums_pb2 as _enums_pb2
import pysteamauth.pb.steammessages_base_pb2 as _steammessages_base_pb2
from pysteamauth.pb.steammessages_unified_base import steamclient_pb2 as _steamclient_pb2


DESCRIPTOR: _descriptor.FileDescriptor
k_EAuthSessionGuardType_DeviceCode: EAuthSessionGuardType
k_EAuthSessionGuardType_DeviceConfirmation: EAuthSessionGuardType
k_EAuthSessionGuardType_EmailCode: EAuthSessionGuardType
k_EAuthSessionGuardType_EmailConfirmation: EAuthSessionGuardType
k_EAuthSessionGuardType_MachineToken: EAuthSessionGuardType
k_EAuthSessionGuardType_None: EAuthSessionGuardType
k_EAuthSessionGuardType_Unknown: EAuthSessionGuardType
k_EAuthSessionSecurityHistory_Invalid: EAuthSessionSecurityHistory
k_EAuthSessionSecurityHistory_NoPriorHistory: EAuthSessionSecurityHistory
k_EAuthSessionSecurityHistory_UsedPreviously: EAuthSessionSecurityHistory
k_EAuthTokenPlatformType_MobileApp: EAuthTokenPlatformType
k_EAuthTokenPlatformType_SteamClient: EAuthTokenPlatformType
k_EAuthTokenPlatformType_Unknown: EAuthTokenPlatformType
k_EAuthTokenPlatformType_WebBrowser: EAuthTokenPlatformType
k_EAuthTokenRevokeConsume: EAuthTokenRevokeAction
k_EAuthTokenRevokeLogout: EAuthTokenRevokeAction
k_EAuthTokenRevokePermanent: EAuthTokenRevokeAction
k_EAuthTokenRevokeReplaced: EAuthTokenRevokeAction
k_EAuthTokenRevokeSupport: EAuthTokenRevokeAction
k_EAuthTokenState_Confirmed: EAuthTokenState
k_EAuthTokenState_Consumed: EAuthTokenState
k_EAuthTokenState_Denied: EAuthTokenState
k_EAuthTokenState_Invalid: EAuthTokenState
k_EAuthTokenState_Issued: EAuthTokenState
k_EAuthTokenState_LoggedOut: EAuthTokenState
k_EAuthTokenState_New: EAuthTokenState
k_EAuthTokenState_Revoked: EAuthTokenState


class CAuthenticationSupport_GetTokenHistory_Request(_message.Message):
    __slots__: List[str] = ['token_id']
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    token_id: int

    def __init__(self, token_id: _Optional[int] = ...) -> None: ...


class CAuthenticationSupport_GetTokenHistory_Response(_message.Message):
    __slots__: List[str] = ['history']
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    history: _containers.RepeatedCompositeFieldContainer[CSupportRefreshTokenAudit]

    def __init__(self, history: _Optional[_Iterable[_Union[CSupportRefreshTokenAudit, _Mapping]]] = ...) -> None: ...


class CAuthenticationSupport_QueryRefreshTokenByID_Request(_message.Message):
    __slots__: List[str] = ['token_id']
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    token_id: int

    def __init__(self, token_id: _Optional[int] = ...) -> None: ...


class CAuthenticationSupport_QueryRefreshTokenByID_Response(_message.Message):
    __slots__: List[str] = ['refresh_tokens']
    REFRESH_TOKENS_FIELD_NUMBER: _ClassVar[int]
    refresh_tokens: _containers.RepeatedCompositeFieldContainer[CSupportRefreshTokenDescription]

    def __init__(self, refresh_tokens: _Optional[
        _Iterable[_Union[CSupportRefreshTokenDescription, _Mapping]]] = ...) -> None: ...


class CAuthenticationSupport_QueryRefreshTokensByAccount_Request(_message.Message):
    __slots__: List[str] = ['include_revoked_tokens', 'steamid']
    INCLUDE_REVOKED_TOKENS_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    include_revoked_tokens: bool
    steamid: int

    def __init__(self, steamid: _Optional[int] = ..., include_revoked_tokens: bool = ...) -> None: ...


class CAuthenticationSupport_QueryRefreshTokensByAccount_Response(_message.Message):
    __slots__: List[str] = ['refresh_tokens']
    REFRESH_TOKENS_FIELD_NUMBER: _ClassVar[int]
    refresh_tokens: _containers.RepeatedCompositeFieldContainer[CSupportRefreshTokenDescription]

    def __init__(self, refresh_tokens: _Optional[
        _Iterable[_Union[CSupportRefreshTokenDescription, _Mapping]]] = ...) -> None: ...


class CAuthenticationSupport_RevokeToken_Request(_message.Message):
    __slots__: List[str] = ['steamid', 'token_id']
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    token_id: int

    def __init__(self, token_id: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...


class CAuthenticationSupport_RevokeToken_Response(_message.Message):
    __slots__: List[str] = []

    def __init__(self) -> None: ...


class CAuthentication_AccessToken_GenerateForApp_Request(_message.Message):
    __slots__: List[str] = ['refresh_token', 'steamid']
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    refresh_token: str
    steamid: int

    def __init__(self, refresh_token: _Optional[str] = ..., steamid: _Optional[int] = ...) -> None: ...


class CAuthentication_AccessToken_GenerateForApp_Response(_message.Message):
    __slots__: List[str] = ['access_token']
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str

    def __init__(self, access_token: _Optional[str] = ...) -> None: ...


class CAuthentication_AllowedConfirmation(_message.Message):
    __slots__: List[str] = ['associated_message', 'confirmation_type']
    ASSOCIATED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONFIRMATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    associated_message: str
    confirmation_type: EAuthSessionGuardType

    def __init__(self, confirmation_type: _Optional[_Union[EAuthSessionGuardType, str]] = ...,
                 associated_message: _Optional[str] = ...) -> None: ...


class CAuthentication_BeginAuthSessionViaCredentials_Request(_message.Message):
    __slots__: List[str] = ['account_name', 'device_details', 'device_friendly_name', 'encrypted_password',
                            'encryption_timestamp',
                            'guard_data', 'language', 'persistence', 'platform_type', 'remember_login', 'website_id']
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    GUARD_DATA_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    PERSISTENCE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
    REMEMBER_LOGIN_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_ID_FIELD_NUMBER: _ClassVar[int]
    account_name: str
    device_details: CAuthentication_DeviceDetails
    device_friendly_name: str
    encrypted_password: str
    encryption_timestamp: int
    guard_data: str
    language: int
    persistence: _enums_pb2.ESessionPersistence
    platform_type: EAuthTokenPlatformType
    remember_login: bool
    website_id: str

    def __init__(self, device_friendly_name: _Optional[str] = ..., account_name: _Optional[str] = ...,
                 encrypted_password: _Optional[str] = ..., encryption_timestamp: _Optional[int] = ...,
                 remember_login: bool = ..., platform_type: _Optional[_Union[EAuthTokenPlatformType, str]] = ...,
                 persistence: _Optional[_Union[_enums_pb2.ESessionPersistence, str]] = ...,
                 website_id: _Optional[str] = ...,
                 device_details: _Optional[_Union[CAuthentication_DeviceDetails, _Mapping]] = ...,
                 guard_data: _Optional[str] = ..., language: _Optional[int] = ...) -> None: ...


class CAuthentication_BeginAuthSessionViaCredentials_Response(_message.Message):
    __slots__: List[str] = ['agreement_session_url', 'allowed_confirmations', 'client_id', 'extended_error_message',
                            'interval',
                            'request_id', 'steamid', 'weak_token']
    AGREEMENT_SESSION_URL_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_CONFIRMATIONS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    WEAK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    agreement_session_url: str
    allowed_confirmations: _containers.RepeatedCompositeFieldContainer[CAuthentication_AllowedConfirmation]
    client_id: int
    extended_error_message: str
    interval: float
    request_id: bytes
    steamid: int
    weak_token: str

    def __init__(self, client_id: _Optional[int] = ..., request_id: _Optional[bytes] = ...,
                 interval: _Optional[float] = ..., allowed_confirmations: _Optional[
                _Iterable[_Union[CAuthentication_AllowedConfirmation, _Mapping]]] = ..., steamid: _Optional[int] = ...,
                 weak_token: _Optional[str] = ..., agreement_session_url: _Optional[str] = ...,
                 extended_error_message: _Optional[str] = ...) -> None: ...


class CAuthentication_BeginAuthSessionViaQR_Request(_message.Message):
    __slots__: List[str] = ['device_details', 'device_friendly_name', 'platform_type', 'website_id']
    DEVICE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_ID_FIELD_NUMBER: _ClassVar[int]
    device_details: CAuthentication_DeviceDetails
    device_friendly_name: str
    platform_type: EAuthTokenPlatformType
    website_id: str

    def __init__(self, device_friendly_name: _Optional[str] = ...,
                 platform_type: _Optional[_Union[EAuthTokenPlatformType, str]] = ...,
                 device_details: _Optional[_Union[CAuthentication_DeviceDetails, _Mapping]] = ...,
                 website_id: _Optional[str] = ...) -> None: ...


class CAuthentication_BeginAuthSessionViaQR_Response(_message.Message):
    __slots__: List[str] = ['allowed_confirmations', 'challenge_url', 'client_id', 'interval', 'request_id', 'version']
    ALLOWED_CONFIRMATIONS_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    allowed_confirmations: _containers.RepeatedCompositeFieldContainer[CAuthentication_AllowedConfirmation]
    challenge_url: str
    client_id: int
    interval: float
    request_id: bytes
    version: int

    def __init__(self, client_id: _Optional[int] = ..., challenge_url: _Optional[str] = ...,
                 request_id: _Optional[bytes] = ..., interval: _Optional[float] = ..., allowed_confirmations: _Optional[
                _Iterable[_Union[CAuthentication_AllowedConfirmation, _Mapping]]] = ...,
                 version: _Optional[int] = ...) -> None: ...


class CAuthentication_DeviceDetails(_message.Message):
    __slots__: List[str] = ['device_friendly_name', 'gaming_device_type', 'os_type', 'platform_type']
    DEVICE_FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    GAMING_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
    device_friendly_name: str
    gaming_device_type: int
    os_type: int
    platform_type: EAuthTokenPlatformType

    def __init__(self, device_friendly_name: _Optional[str] = ...,
                 platform_type: _Optional[_Union[EAuthTokenPlatformType, str]] = ..., os_type: _Optional[int] = ...,
                 gaming_device_type: _Optional[int] = ...) -> None: ...


class CAuthentication_GetAuthSessionInfo_Request(_message.Message):
    __slots__: List[str] = ['client_id']
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: int

    def __init__(self, client_id: _Optional[int] = ...) -> None: ...


class CAuthentication_GetAuthSessionInfo_Response(_message.Message):
    __slots__: List[str] = ['city', 'country', 'device_friendly_name', 'geoloc', 'high_usage_login', 'ip',
                            'login_history',
                            'platform_type', 'requested_persistence', 'requestor_location_mismatch', 'state', 'version']
    CITY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    GEOLOC_FIELD_NUMBER: _ClassVar[int]
    HIGH_USAGE_LOGIN_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    LOGIN_HISTORY_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_PERSISTENCE_FIELD_NUMBER: _ClassVar[int]
    REQUESTOR_LOCATION_MISMATCH_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    city: str
    country: str
    device_friendly_name: str
    geoloc: str
    high_usage_login: bool
    ip: str
    login_history: EAuthSessionSecurityHistory
    platform_type: EAuthTokenPlatformType
    requested_persistence: _enums_pb2.ESessionPersistence
    requestor_location_mismatch: bool
    state: str
    version: int

    def __init__(self, ip: _Optional[str] = ..., geoloc: _Optional[str] = ..., city: _Optional[str] = ...,
                 state: _Optional[str] = ..., country: _Optional[str] = ...,
                 platform_type: _Optional[_Union[EAuthTokenPlatformType, str]] = ...,
                 device_friendly_name: _Optional[str] = ..., version: _Optional[int] = ...,
                 login_history: _Optional[_Union[EAuthSessionSecurityHistory, str]] = ...,
                 requestor_location_mismatch: bool = ..., high_usage_login: bool = ...,
                 requested_persistence: _Optional[_Union[_enums_pb2.ESessionPersistence, str]] = ...) -> None: ...


class CAuthentication_GetAuthSessionsForAccount_Request(_message.Message):
    __slots__: List[str] = []

    def __init__(self) -> None: ...


class CAuthentication_GetAuthSessionsForAccount_Response(_message.Message):
    __slots__: List[str] = ['client_ids']
    CLIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    client_ids: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, client_ids: _Optional[_Iterable[int]] = ...) -> None: ...


class CAuthentication_GetPasswordRSAPublicKey_Request(_message.Message):
    __slots__: List[str] = ['account_name']
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    account_name: str

    def __init__(self, account_name: _Optional[str] = ...) -> None: ...


class CAuthentication_GetPasswordRSAPublicKey_Response(_message.Message):
    __slots__: List[str] = ['publickey_exp', 'publickey_mod', 'timestamp']
    PUBLICKEY_EXP_FIELD_NUMBER: _ClassVar[int]
    PUBLICKEY_MOD_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    publickey_exp: str
    publickey_mod: str
    timestamp: int

    def __init__(self, publickey_mod: _Optional[str] = ..., publickey_exp: _Optional[str] = ...,
                 timestamp: _Optional[int] = ...) -> None: ...


class CAuthentication_MigrateMobileSession_Request(_message.Message):
    __slots__: List[str] = ['signature', 'steamid', 'token']
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    signature: str
    steamid: int
    token: str

    def __init__(self, steamid: _Optional[int] = ..., token: _Optional[str] = ...,
                 signature: _Optional[str] = ...) -> None: ...


class CAuthentication_MigrateMobileSession_Response(_message.Message):
    __slots__: List[str] = ['access_token', 'refresh_token']
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str

    def __init__(self, refresh_token: _Optional[str] = ..., access_token: _Optional[str] = ...) -> None: ...


class CAuthentication_PollAuthSessionStatus_Request(_message.Message):
    __slots__: List[str] = ['client_id', 'request_id', 'token_to_revoke']
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TO_REVOKE_FIELD_NUMBER: _ClassVar[int]
    client_id: int
    request_id: bytes
    token_to_revoke: int

    def __init__(self, client_id: _Optional[int] = ..., request_id: _Optional[bytes] = ...,
                 token_to_revoke: _Optional[int] = ...) -> None: ...


class CAuthentication_PollAuthSessionStatus_Response(_message.Message):
    __slots__: List[str] = [
        'access_token',
        'account_name',
        'had_remote_interaction',
        'new_challenge_url',
        'new_client_id',
        'new_guard_data',
        'refresh_token'
    ]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    HAD_REMOTE_INTERACTION_FIELD_NUMBER: _ClassVar[int]
    NEW_CHALLENGE_URL_FIELD_NUMBER: _ClassVar[int]
    NEW_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_GUARD_DATA_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    account_name: str
    had_remote_interaction: bool
    new_challenge_url: str
    new_client_id: int
    new_guard_data: str
    refresh_token: str

    def __init__(self, new_client_id: _Optional[int] = ..., new_challenge_url: _Optional[str] = ...,
                 refresh_token: _Optional[str] = ..., access_token: _Optional[str] = ...,
                 had_remote_interaction: bool = ..., account_name: _Optional[str] = ...,
                 new_guard_data: _Optional[str] = ...) -> None: ...


class CAuthentication_RefreshToken_Enumerate_Request(_message.Message):
    __slots__: List[str] = []

    def __init__(self) -> None: ...


class CAuthentication_RefreshToken_Enumerate_Response(_message.Message):
    __slots__: List[str] = ['refresh_tokens', 'requesting_token']

    class RefreshTokenDescription(_message.Message):
        __slots__: List[str] = ['auth_type', 'first_seen', 'gaming_device_type', 'last_seen', 'logged_in',
                                'os_platform',
                                'os_type', 'platform_type', 'time_updated', 'token_description', 'token_id']
        AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
        FIRST_SEEN_FIELD_NUMBER: _ClassVar[int]
        GAMING_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        LAST_SEEN_FIELD_NUMBER: _ClassVar[int]
        LOGGED_IN_FIELD_NUMBER: _ClassVar[int]
        OS_PLATFORM_FIELD_NUMBER: _ClassVar[int]
        OS_TYPE_FIELD_NUMBER: _ClassVar[int]
        PLATFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
        TIME_UPDATED_FIELD_NUMBER: _ClassVar[int]
        TOKEN_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
        auth_type: int
        first_seen: CAuthentication_RefreshToken_Enumerate_Response.TokenUsageEvent
        gaming_device_type: int
        last_seen: CAuthentication_RefreshToken_Enumerate_Response.TokenUsageEvent
        logged_in: bool
        os_platform: int
        os_type: int
        platform_type: EAuthTokenPlatformType
        time_updated: int
        token_description: str
        token_id: int

        def __init__(self, token_id: _Optional[int] = ..., token_description: _Optional[str] = ...,
                     time_updated: _Optional[int] = ...,
                     platform_type: _Optional[_Union[EAuthTokenPlatformType, str]] = ..., logged_in: bool = ...,
                     os_platform: _Optional[int] = ..., auth_type: _Optional[int] = ...,
                     gaming_device_type: _Optional[int] = ..., first_seen: _Optional[
                    _Union[CAuthentication_RefreshToken_Enumerate_Response.TokenUsageEvent, _Mapping]] = ...,
                     last_seen: _Optional[
                         _Union[CAuthentication_RefreshToken_Enumerate_Response.TokenUsageEvent, _Mapping]] = ...,
                     os_type: _Optional[int] = ...) -> None: ...

    class TokenUsageEvent(_message.Message):
        __slots__: List[str] = ['city', 'country', 'ip', 'locale', 'state', 'time']
        CITY_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        city: str
        country: str
        ip: _steammessages_base_pb2.CMsgIPAddress
        locale: str
        state: str
        time: int

        def __init__(self, time: _Optional[int] = ...,
                     ip: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ...,
                     locale: _Optional[str] = ..., country: _Optional[str] = ..., state: _Optional[str] = ...,
                     city: _Optional[str] = ...) -> None: ...

    REFRESH_TOKENS_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_TOKEN_FIELD_NUMBER: _ClassVar[int]
    refresh_tokens: _containers.RepeatedCompositeFieldContainer[
        CAuthentication_RefreshToken_Enumerate_Response.RefreshTokenDescription]
    requesting_token: int

    def __init__(self, refresh_tokens: _Optional[
        _Iterable[_Union[CAuthentication_RefreshToken_Enumerate_Response.RefreshTokenDescription, _Mapping]]] = ...,
                 requesting_token: _Optional[int] = ...) -> None: ...


class CAuthentication_RefreshToken_Revoke_Request(_message.Message):
    __slots__: List[str] = ['revoke_action', 'signature', 'steamid', 'token_id']
    REVOKE_ACTION_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    revoke_action: EAuthTokenRevokeAction
    signature: bytes
    steamid: int
    token_id: int

    def __init__(self, token_id: _Optional[int] = ..., steamid: _Optional[int] = ...,
                 revoke_action: _Optional[_Union[EAuthTokenRevokeAction, str]] = ...,
                 signature: _Optional[bytes] = ...) -> None: ...


class CAuthentication_RefreshToken_Revoke_Response(_message.Message):
    __slots__: List[str] = []

    def __init__(self) -> None: ...


class CAuthentication_UpdateAuthSessionWithMobileConfirmation_Request(_message.Message):
    __slots__: List[str] = ['client_id', 'confirm', 'persistence', 'signature', 'steamid', 'version']
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_FIELD_NUMBER: _ClassVar[int]
    PERSISTENCE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    client_id: int
    confirm: bool
    persistence: _enums_pb2.ESessionPersistence
    signature: bytes
    steamid: int
    version: int

    def __init__(self, version: _Optional[int] = ..., client_id: _Optional[int] = ..., steamid: _Optional[int] = ...,
                 signature: _Optional[bytes] = ..., confirm: bool = ...,
                 persistence: _Optional[_Union[_enums_pb2.ESessionPersistence, str]] = ...) -> None: ...


class CAuthentication_UpdateAuthSessionWithMobileConfirmation_Response(_message.Message):
    __slots__: List[str] = []

    def __init__(self) -> None: ...


class CAuthentication_UpdateAuthSessionWithSteamGuardCode_Request(_message.Message):
    __slots__: List[str] = ['client_id', 'code', 'code_type', 'steamid']
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    client_id: int
    code: str
    code_type: EAuthSessionGuardType
    steamid: int

    def __init__(self, client_id: _Optional[int] = ..., steamid: _Optional[int] = ..., code: _Optional[str] = ...,
                 code_type: _Optional[_Union[EAuthSessionGuardType, str]] = ...) -> None: ...


class CAuthentication_UpdateAuthSessionWithSteamGuardCode_Response(_message.Message):
    __slots__: List[str] = ['agreement_session_url']
    AGREEMENT_SESSION_URL_FIELD_NUMBER: _ClassVar[int]
    agreement_session_url: str

    def __init__(self, agreement_session_url: _Optional[str] = ...) -> None: ...


class CCloudGaming_CreateNonce_Request(_message.Message):
    __slots__: List[str] = ['appid', 'platform']
    APPID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    appid: int
    platform: str

    def __init__(self, platform: _Optional[str] = ..., appid: _Optional[int] = ...) -> None: ...


class CCloudGaming_CreateNonce_Response(_message.Message):
    __slots__: List[str] = ['expiry', 'nonce']
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    expiry: int
    nonce: str

    def __init__(self, nonce: _Optional[str] = ..., expiry: _Optional[int] = ...) -> None: ...


class CCloudGaming_GetTimeRemaining_Request(_message.Message):
    __slots__: List[str] = ['appid_list', 'platform']
    APPID_LIST_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    appid_list: _containers.RepeatedScalarFieldContainer[int]
    platform: str

    def __init__(self, platform: _Optional[str] = ..., appid_list: _Optional[_Iterable[int]] = ...) -> None: ...


class CCloudGaming_GetTimeRemaining_Response(_message.Message):
    __slots__: List[str] = ['entries']
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CCloudGaming_TimeRemaining]

    def __init__(self, entries: _Optional[_Iterable[_Union[CCloudGaming_TimeRemaining, _Mapping]]] = ...) -> None: ...


class CCloudGaming_TimeRemaining(_message.Message):
    __slots__: List[str] = ['appid', 'minutes_remaining']
    APPID_FIELD_NUMBER: _ClassVar[int]
    MINUTES_REMAINING_FIELD_NUMBER: _ClassVar[int]
    appid: int
    minutes_remaining: int

    def __init__(self, appid: _Optional[int] = ..., minutes_remaining: _Optional[int] = ...) -> None: ...


class CSupportRefreshTokenAudit(_message.Message):
    __slots__: List[str] = ['action', 'actor', 'ip', 'time']
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    action: int
    actor: int
    ip: _steammessages_base_pb2.CMsgIPAddress
    time: int

    def __init__(self, action: _Optional[int] = ..., time: _Optional[int] = ...,
                 ip: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ...,
                 actor: _Optional[int] = ...) -> None: ...


class CSupportRefreshTokenDescription(_message.Message):
    __slots__: List[str] = ['auth_type', 'first_seen', 'gaming_device_type', 'last_seen', 'os_platform', 'os_type',
                            'owner_steamid', 'platform_type', 'time_updated', 'token_description', 'token_id',
                            'token_state']

    class TokenUsageEvent(_message.Message):
        __slots__: List[str] = ['city', 'country', 'ip', 'state', 'time']
        CITY_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        city: str
        country: str
        ip: _steammessages_base_pb2.CMsgIPAddress
        state: str
        time: int

        def __init__(self, time: _Optional[int] = ...,
                     ip: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ...,
                     country: _Optional[str] = ..., state: _Optional[str] = ...,
                     city: _Optional[str] = ...) -> None: ...

    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEEN_FIELD_NUMBER: _ClassVar[int]
    GAMING_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_FIELD_NUMBER: _ClassVar[int]
    OS_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    OWNER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_UPDATED_FIELD_NUMBER: _ClassVar[int]
    TOKEN_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_STATE_FIELD_NUMBER: _ClassVar[int]
    auth_type: int
    first_seen: CSupportRefreshTokenDescription.TokenUsageEvent
    gaming_device_type: int
    last_seen: CSupportRefreshTokenDescription.TokenUsageEvent
    os_platform: int
    os_type: int
    owner_steamid: int
    platform_type: EAuthTokenPlatformType
    time_updated: int
    token_description: str
    token_id: int
    token_state: EAuthTokenState

    def __init__(self, token_id: _Optional[int] = ..., token_description: _Optional[str] = ...,
                 time_updated: _Optional[int] = ...,
                 platform_type: _Optional[_Union[EAuthTokenPlatformType, str]] = ...,
                 token_state: _Optional[_Union[EAuthTokenState, str]] = ..., owner_steamid: _Optional[int] = ...,
                 os_platform: _Optional[int] = ..., os_type: _Optional[int] = ..., auth_type: _Optional[int] = ...,
                 gaming_device_type: _Optional[int] = ...,
                 first_seen: _Optional[_Union[CSupportRefreshTokenDescription.TokenUsageEvent, _Mapping]] = ...,
                 last_seen: _Optional[
                     _Union[CSupportRefreshTokenDescription.TokenUsageEvent, _Mapping]] = ...) -> None: ...


class EAuthTokenPlatformType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__: List[str] = [
        'k_EAuthTokenPlatformType_MobileApp',
        'k_EAuthTokenPlatformType_SteamClient',
        'k_EAuthTokenPlatformType_WebBrowser',
    ]


class EAuthSessionGuardType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__: List[str] = []


class EAuthSessionSecurityHistory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__: List[str] = []


class EAuthTokenRevokeAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__: List[str] = []


class EAuthTokenState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__: List[str] = []
