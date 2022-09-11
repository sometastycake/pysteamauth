from yarl import URL


def get_host_from_url(url: str) -> str:
    return URL(url).host.replace('www.', '')
