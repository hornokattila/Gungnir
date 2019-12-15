import base64
import sys
import typing


class LoginManager:
    def kernel_loader(self, headers: typing.Dict[str, str]) -> None:
        try:
            getattr(self, "_kernel_{0}".format(sys.platform))(*base64.b64decode(headers.get("Authorization").replace("Basic ", "", 1)).decode().split(":"))
        except (AttributeError, TypeError, ValueError):
            raise PermissionError()

    def vacant_loader(self, headers: typing.Dict[str, str]) -> None:
        pass

    def _kernel_linux(self, username: str, password: str) -> None:
        raise NotImplementedError()

    def _kernel_win32(self, username: str, password: str) -> None:
        raise NotImplementedError()
