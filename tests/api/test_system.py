from gungnir.api.system import system
from tests.TestUtil import TestUtil


class TestDevice:
    def test_system(self) -> None:
        assert TestUtil.view_func(system, "/system") == "{}"
