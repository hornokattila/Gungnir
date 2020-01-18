import base64
import sys
import typing


class LoginManager:
    def shadow_loader(self, headers: typing.Dict[str, str]) -> None:
        try:
            getattr(self, "_shadow_{0}".format(sys.platform))(*base64.b64decode(headers.get("Authorization").replace("Basic ", "", 1)).decode().split(":"))
        except (AttributeError, TypeError, ValueError):
            raise PermissionError()

    def vacant_loader(self, headers: typing.Dict[str, str]) -> None:
        pass

    def _shadow_linux(self, username: str, password: str) -> None:
        raise NotImplementedError()

    def _shadow_win32(self, username: str, password: str) -> None:
        raise NotImplementedError()
