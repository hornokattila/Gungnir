import base64
import typing


class LoginManager:
    def ba_spwd(self, headers: typing.Dict[str, str]) -> None:
        try:
            credentials: typing.List[str] = []
            for data in headers.get("Authorization").replace("Basic ", "", 1).split(":"):
                credentials.append(base64.b64decode(data))
        except TypeError:
            pass
