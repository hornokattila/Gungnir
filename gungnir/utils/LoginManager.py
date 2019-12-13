import base64
import sys
import typing


class LoginManager:
    def system_loader(self, headers: typing.Dict[str, str]) -> None:
        try:
            getattr(self, "_sys_{0}".format(sys.platform))(*base64.b64decode(headers.get("Authorization").replace("Basic ", "", 1)).decode().split(":"))
        except (AttributeError, TypeError, ValueError):
            raise PermissionError()

    def vacant_loader(self, headers: typing.Dict[str, str]) -> None:
        pass

    def _sys_linux(self, username: str, password: str) -> None:
        # TODO: Missing implementation!
        pass

    def _sys_win32(self, username: str, password: str) -> None:
        raise NotImplementedError()
