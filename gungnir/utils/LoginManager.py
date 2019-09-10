import base64
import typing


class LoginManager:
    def ba_spwd(self, headers: typing.Dict[str, str]) -> None:
        try:
            api_key: typing.List[str] = []
            for data in headers.get("Authorization").replace("Basic ", "", 1).split(":"):
                api_key.append(base64.b64decode(data))
        except TypeError:
            pass
