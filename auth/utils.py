from yarl import URL


def _get_host_from_url(url: str) -> str:
    return URL(url).host.replace('www.', '')
