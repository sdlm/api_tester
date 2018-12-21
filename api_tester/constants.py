from api_tester.utils import make_namedtuple

ENVIRONMENT = 'test'  # 'prod'


DOMAIN = make_namedtuple(
    FIRST='first.com',
    SECOND='second.com',
)
