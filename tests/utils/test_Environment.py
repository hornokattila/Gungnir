import sys
import typing

from gungnir.utils.Environment import Environment
from tests.TestUtil import TestUtil


class TestEnvironment:
    def test_decode(self) -> None:
        sys.platform = "dummy"
        assert TestUtil.catch(Environment.RUNNER.decode) == ProcessLookupError
        runner: typing.Dict[str, str] = Environment.RUNNER.value
        for key in runner.keys():
            sys.platform = key
            assert TestUtil.catch(Environment.RUNNER.decode) == runner[key]
