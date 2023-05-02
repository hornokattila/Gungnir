import base64
import importlib
import sys
import typing


class LoginManager:
    def shadow_loader(self, headers: typing.Dict[str, str]) -> None:
        try:
            getattr(self, "_shadow_{0}".format(sys.platform))(*base64.b64decode(headers.get("Authorization").replace("Basic ", "", 1)).decode().split(":"))
        except (AttributeError, TypeError, ValueError):
            raise PermissionError()

    def _shadow_darwin(self, username: str, password: str) -> None:
        # TODO: Add authentication for MacOS.
        pass

    def _shadow_linux(self, username: str, password: str) -> None:
        sp_pwdp: str = importlib.import_module("spwd").getspnam(username).sp_pwdp
        if sp_pwdp.__ne__(importlib.import_module("crypt").crypt(password, sp_pwdp)):
            raise PermissionError()

    def _shadow_win32(self, username: str, password: str) -> None:
        # TODO: Add authentication for Windows.
        pass
