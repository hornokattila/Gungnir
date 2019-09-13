import base64
import typing


# TODO: Work in progress!
class LoginManager:
    def ba_spwd(self, headers: typing.Dict[str, str]) -> None:
        try:
            credentials: typing.List[str] = base64.b64decode(headers.get("Authorization").replace("Basic ", "", 1)).decode().split(":")
        except TypeError:
            pass
