from collections import namedtuple

import requests


def http_get(*args, auth=True, **kwargs):
    return requests.get(
        *args, **kwargs
    )


def http_post(*args, auth=True, **kwargs):
    return requests.post(
        *args, **kwargs
    )


def make_namedtuple(title=None, **kwargs):
    domain_cls = namedtuple(title or 'namedtuple', kwargs.keys())
    return domain_cls(**kwargs)
