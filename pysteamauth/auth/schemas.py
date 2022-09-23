from typing import (
    List,
    Optional,
)

from pydantic import BaseModel


class AuthenticatorData(BaseModel):
    shared_secret: str
    identity_secret: str
    device_id: str


class Params(BaseModel):
    nonce: str
    auth: str


class TransferInfoItem(BaseModel):
    url: str
    params: Params


class FinalizeLoginStatus(BaseModel):
    steamID: str
    redir: str
    transfer_info: List[TransferInfoItem]
    primary_domain: str


class ServerTime(BaseModel):
    server_time: int
    skew_tolerance_seconds: int
    large_time_jink: int
    probe_frequency_seconds: int
    adjusted_time_probe_frequency_seconds: int
    hint_probe_frequency_seconds: int
    sync_timeout: int
    try_again_seconds: int
    max_attempts: int


class ServerTimeResponse(BaseModel):
    response: ServerTime


class SteamAuthorizationStatus(BaseModel):
    logged_in: bool
    steamid: str
    accountid: int
    account_name: str
    token: Optional[str]
