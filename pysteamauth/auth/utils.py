import base64

from google.protobuf.message import Message

from pysteamauth.pb.steammessages_auth.steamclient_pb2 import (
    EAuthTokenPlatformType,
    k_EAuthTokenPlatformType_MobileApp,
    k_EAuthTokenPlatformType_SteamClient,
    k_EAuthTokenPlatformType_WebBrowser,
)


def pbmessage_to_request(msg: Message) -> str:
    return str(base64.b64encode(msg.SerializeToString()), 'utf8')


def platform_to_str(platform: EAuthTokenPlatformType) -> str:
    if platform == k_EAuthTokenPlatformType_MobileApp:
        return 'mobile'
    elif platform == k_EAuthTokenPlatformType_SteamClient:
        return 'steam_client'
    elif platform == k_EAuthTokenPlatformType_WebBrowser:
        return 'web_browser'
    else:
        raise ValueError('Unknown platform type')


def get_website_id_by_platform(platform: EAuthTokenPlatformType) -> str:
    if platform == k_EAuthTokenPlatformType_MobileApp:
        return 'Mobile'
    elif platform == k_EAuthTokenPlatformType_SteamClient:
        return 'Client'
    elif platform == k_EAuthTokenPlatformType_WebBrowser:
        return 'Community'
    else:
        raise ValueError('Unknown platform type')
