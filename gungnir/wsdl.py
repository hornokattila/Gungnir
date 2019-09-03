import typing

import flask

from utils.Blueprint import Blueprint


class Flask(flask.Flask):
    def run(self, **options: typing.Union[str, typing.Dict[str, typing.Union[bool, int, str]], typing.List[Blueprint]]) -> None:
        url_prefix: str = options.pop("url_prefix")
        for url in options.pop("urls"):
            super().register_blueprint(url, url_prefix=url_prefix)
        super().run(**options)
