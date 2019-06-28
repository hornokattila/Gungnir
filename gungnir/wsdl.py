import typing

import flask

from util.Blueprint import Blueprint


class Flask(flask.Flask):
    def run(self, **options: typing.Union[str, typing.Dict[str, typing.Union[bool, int, str]], typing.List[Blueprint]]) -> None:
        version: str = options.pop("version")
        for url in options.pop("urls"):
            super().register_blueprint(url, url_prefix=version)
        super().run(**options)
