from typing import (
    List,
    Optional,
)

from pydantic import BaseModel


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


class TokenFirstSeen(BaseModel):
    time: int


class TokenIp(BaseModel):
    v4: Optional[int]
    v6: Optional[int]


class TokenLastSeen(BaseModel):
    time: int
    ip: TokenIp
    country: str
    state: str
    city: str


class RefreshToken(BaseModel):
    token_id: str
    token_description: Optional[str]
    time_updated: int
    platform_type: int
    logged_in: bool
    os_platform: int
    auth_type: int
    first_seen: TokenFirstSeen
    last_seen: TokenLastSeen
    os_type: int


class EnumerateTokensResponse(BaseModel):
    refresh_tokens: List[RefreshToken]


class EnumerateTokensModel(BaseModel):
    response: EnumerateTokensResponse


class LoginResult(BaseModel):
    client_id: int
    refresh_token: str
    access_token: str
