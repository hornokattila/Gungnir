import enum
import sys
import typing


class Environment(enum.Enum):
    RUNNER = {
        "darwin": "zsh",
        "linux": "bash",
        "win32": "powershell"
    }

    def decode(self: typing.Self) -> str:
        try:
            return self.value[sys.platform]
        except KeyError:
            raise ProcessLookupError()
