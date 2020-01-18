import sys


class System:
    @staticmethod
    def call(method: str) -> None:
        try:
            return getattr(System(), "_{0}_{1}".format(method, sys.platform))()
        except AttributeError:
            raise PermissionError()

    def _reboot_linux(self) -> None:
        raise NotImplementedError()

    def _reboot_win32(self) -> None:
        raise NotImplementedError()
