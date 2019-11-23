import typing

import flask

from utils.Blueprint import Blueprint


class Flask(flask.Flask):
    def run(self, **options: typing.Union[str, typing.Dict[str, typing.Union[bool, int, str]], typing.List[Blueprint]]) -> None:
        url_config: typing.Dict[str, typing.Union[bool, int, str]] = options.pop("url_config")
        url_prefix: str = options.pop("url_prefix")
        for prop in options.pop("urls"):
            prop.settings = url_config
            prop.init()
            super().register_blueprint(prop, url_prefix=url_prefix)
        super().run(**options)
