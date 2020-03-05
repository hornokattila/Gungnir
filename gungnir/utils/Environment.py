import enum
import sys


class Environment(enum.Enum):
    REBOOT = {
        "linux": "reboot",
        "win32": "shutdown -r"
    }

    RUNNER = {
        "linux": "bash",
        "win32": "powershell"
    }

    def decode(self) -> str:
        try:
            return self.value[sys.platform]
        except KeyError:
            raise ProcessLookupError()
