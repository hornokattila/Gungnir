import typing

from gungnir.api.device import device
from tests.TestUtil import TestUtil


class TestDevice:
    def test_health(self: typing.Self) -> None:
        assert TestUtil.view_func(device, "/health", "GET") == ""
