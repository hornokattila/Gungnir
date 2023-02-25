import sys

from gungnir.utils.Environment import Environment


class TestEnvironment:
    def test_decode(self) -> None:
        sys.platform = "dummy"
        try:
            Environment.RUNNER.decode()
            assert False
        except ProcessLookupError:
            pass
