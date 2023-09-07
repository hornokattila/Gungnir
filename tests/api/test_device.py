from gungnir.api.device import device
from tests.TestUtil import TestUtil


class TestDevice:
    def test_health(self) -> None:
        assert TestUtil.view_func(device, "/health", "GET") == ""
