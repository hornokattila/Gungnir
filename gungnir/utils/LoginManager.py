import base64
import sys
import typing


class LoginManager:
    def basicAuthAgainstSysInfo(self, headers: typing.Dict[str, str]) -> None:
        try:
            getattr(self, "_sys_{0}".format(sys.platform))(base64.b64decode(headers.get("Authorization").replace("Basic ", "", 1)).decode().split(":"))
        except (AttributeError, ValueError):
            pass

    def _sys_linux(self, credentials: typing.Dict[str, str]) -> None:
        pass

    def _sys_win32(self, credentials: typing.Dict[str, str]) -> None:
        pass
