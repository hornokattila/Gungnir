import sys
import typing

from gungnir.utils.Environment import Environment
from tests.TestUtil import TestUtil


class TestEnvironment:
    def setup_method(self, method):
        if method.__name__ == "test_decode":
            self.platform: str = sys.platform
            sys.platform = "dummy"

    def teardown_method(self, method):
        if method.__name__ == "test_decode":
            sys.platform = self.platform

    def test_decode(self) -> None:
        assert TestUtil.catch(Environment.RUNNER.decode) == ProcessLookupError
        runner: typing.Dict[str, str] = Environment.RUNNER.value
        for key in runner.keys():
            sys.platform = key
            assert TestUtil.catch(Environment.RUNNER.decode) == runner[key]
