from api_tester.constants import DOMAIN
from api_tester.utils import http_get


def test_endpoint():
    resp = http_get(f'http://{DOMAIN}/endpoint')
    assert resp.status_code == 200
