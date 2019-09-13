import base64
import typing


# TODO: Work in progress!
class LoginManager:
    def ba_spwd(self, headers: typing.Dict[str, str]) -> None:
        try:
            credentials: typing.List[str] = list(map(lambda code: base64.b64decode(code), headers.get("Authorization").replace("Basic ", "", 1).split(":")))
        except TypeError:
            pass
