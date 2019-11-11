import base64
import sys
import typing


class LoginManager:
    def user_loader(self, headers: typing.Dict[str, str]) -> None:
        try:
            getattr(self, "_sys_{0}".format(sys.platform))(*base64.b64decode(headers.get("Authorization").replace("Basic ", "", 1)).decode().split(":"))
        except (AttributeError, ValueError):
            raise ProcessLookupError()

    def _sys_linux(self, username: str, password: str) -> None:
        raise NotImplementedError()

    def _sys_win32(self, username: str, password: str) -> None:
        raise NotImplementedError()
