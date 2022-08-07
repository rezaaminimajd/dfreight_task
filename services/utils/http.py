import requests
from typing import Union, Any, Dict


def request(
        method: str,
        url: str,
        params: Dict[str, Union[str, int, float]] = None,
        json: Dict[str, Any] = None,
        headers: Dict[str, Union[str, int, float]] = None,
        cookies: Dict[str, Union[str, int, float]] = None,
        retry_count: int = 0,
        proxies: Dict[str, str] = None
) -> requests.Response:
    params = {} if not params else params
    json = {} if not json else json

    assert retry_count >= 0, "retry_count must be non-negative"

    response = None
    while retry_count > -1:

        response = requests.request(
            method=method,
            url=url,
            params=params,
            json=json,
            headers=headers,
            cookies=cookies,
            proxies=proxies
        )
        status_code = response.status_code
        retry_count -= 1
        if 200 <= status_code < 300:
            break

    return response
