from api import health


def test_health():
    assert health._health().__eq__("")
