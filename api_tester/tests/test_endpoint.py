from api_tester.constants import DOMAIN
from api_tester.utils import http_get


def test_endpoint_1():
    resp = http_get(f'http://{DOMAIN.FIRST}/endpoint')
    assert resp.status_code == 200
    resp_data = resp.json()
    assert isinstance(resp_data, dict)


def test_endpoint_2():
    resp = http_get(f'http://{DOMAIN.FIRST}/other_endpoint')
    assert resp.status_code == 200
