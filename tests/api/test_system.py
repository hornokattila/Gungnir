import typing

from gungnir.api.system import system
from tests.TestUtil import TestUtil


class TestSystem:
    def test_system(self: typing.Self) -> None:
        assert TestUtil.view_func(system, "/system", "GET") == "{}"
