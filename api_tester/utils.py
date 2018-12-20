import requests


def http_get(*args, auth=True, **kwargs):
    return requests.get(
        *args, **kwargs
    )


def http_post(*args, auth=True, **kwargs):
    return requests.post(
        *args, **kwargs
    )
