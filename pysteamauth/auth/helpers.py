import base64
import random
from typing import Dict

from aiohttp.abc import AbstractCookieJar
from google.protobuf.message import Message
from yarl import URL

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


def get_cookies_by_url(cookie_jar: AbstractCookieJar, url: URL) -> Dict[str, str]:
    cookies = cookie_jar.filter_cookies(url)
    return {name: cookie.value for name, cookie in cookies.items()}


def get_cookies(cookie_jar: AbstractCookieJar) -> Dict[str, Dict[str, str]]:
    cookies = {}
    for cookie in cookie_jar:
        domain = cookie['domain']
        if domain not in cookies:
            cookies[domain] = {}
        cookies[domain].update({cookie.key: cookie.value})
    return cookies


def generate_sessionid() -> str:
    choices = '0123456789abcdef'
    return ''.join([random.choice(choices) for _ in range(24)])
