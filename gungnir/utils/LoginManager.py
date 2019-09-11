import base64
import typing


# TODO: Work in progress!
class LoginManager:
    def ba_spwd(self, headers: typing.Dict[str, str]) -> None:
        try:
            credentials: typing.List[str] = []
            for code in headers.get("Authorization").replace("Basic ", "", 1).split(":"):
                credentials.append(base64.b64decode(code))
        except TypeError:
            pass
