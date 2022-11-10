import enum
import sys


class Environment(enum.Enum):
    RUNNER = {
        "darwin": "zsh",
        "linux": "bash",
        "win32": "powershell"
    }

    def decode(self) -> str:
        try:
            return self.value[sys.platform]
        except KeyError:
            raise ProcessLookupError()
