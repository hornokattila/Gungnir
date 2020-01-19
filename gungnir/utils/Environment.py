import enum
import sys


class Environment(enum.Enum):
    REBOOT = {"linux": "reboot"}

    def decode(self) -> str:
        try:
            return self.value[sys.platform]
        except KeyError:
            raise ProcessLookupError()
