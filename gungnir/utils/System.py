import os
import sys
import time
from concurrent.futures.thread import ThreadPoolExecutor


class System:
    @staticmethod
    def call(method: str) -> None:
        try:
            return getattr(System(), "_{0}_{1}".format(method, sys.platform))()
        except AttributeError:
            raise PermissionError()

    def _reboot_linux(self) -> None:
        executor: ThreadPoolExecutor = ThreadPoolExecutor(1)
        executor.submit(time.sleep, 2)
        executor.submit(os.system, "reboot")

    def _reboot_win32(self) -> None:
        raise NotImplementedError()
