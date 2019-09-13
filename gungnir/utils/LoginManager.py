import base64
import sys
import typing


# TODO: Work in progress!
class LoginManager:
    def ba_spwd(self, headers: typing.Dict[str, str]) -> None:
        try:
            getattr(self, sys.platform)(base64.b64decode(headers.get("Authorization").replace("Basic ", "", 1)).decode().split(":"))
        except TypeError:
            pass

    def linux(self, credentials: typing.Dict[str, str]) -> None:
        pass

    def win32(self, credentials: typing.Dict[str, str]) -> None:
        pass
