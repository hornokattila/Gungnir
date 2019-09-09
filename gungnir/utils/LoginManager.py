import base64
import typing


class LoginManager:
    def ba_spwd(self, headers: typing.Dict[str, str]) -> None:
        try:
            api_key: str = base64.b64decode(headers["Authorization"].replace("Basic ", "", 1))
        except (KeyError, TypeError):
            pass
