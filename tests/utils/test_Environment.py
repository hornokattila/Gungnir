import sys

from gungnir.utils.Environment import Environment
from tests.TestUtil import TestUtil


class TestEnvironment:
    def test_decode(self) -> None:
        sys.platform = "dummy"
        assert TestUtil.catch(Environment.RUNNER.decode) == ProcessLookupError
        sys.platform = "linux"
        assert TestUtil.catch(Environment.RUNNER.decode) == "bash"
