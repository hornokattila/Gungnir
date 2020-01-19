import enum
import sys


class Environment(enum.Enum):
    REBOOT = {"linux": "reboot"}

    def decode(self) -> str:
        return self.value[sys.platform]
