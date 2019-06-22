import typing

import flask


class Flask(flask.Flask):
    def run(self: typing.Type["Flask"], **options: typing.Union[str, typing.Dict[str, typing.Union[bool, int, str]], typing.List[flask.Blueprint]]) -> None:
        version = options.pop("version")
        for url in options.pop("urls"):
            super().register_blueprint(url, url_prefix=version)
        super().run(**options)
