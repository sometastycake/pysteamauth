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


class SteamAuthorizationStatus(BaseModel):
    logged_in: bool
    steamid: str
    accountid: int
    account_name: str
    token: Optional[str]
