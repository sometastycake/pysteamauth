from yarl import URL


def get_host_from_url(url: str) -> str:
    host = URL(url).host
    if not host:
        raise RuntimeError(f'Wrong url {url}')
    return host.replace('www.', '')
