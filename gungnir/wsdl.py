import typing

import flask

from gungnir.utils.Blueprint import Blueprint


class Flask(flask.Flask):
    def run(self, **options: typing.Union[str, typing.Dict[str, typing.Union[bool, int, str]], typing.List[Blueprint]]) -> None:
        url_config: typing.Dict[str, typing.Union[bool, int, str]] = options.pop("url_config")
        url_prefix: str = options.pop("url_prefix")
        url_system: typing.Dict[str, typing.Union[bool, int, str]] = options.pop("url_system")
        urls: typing.List[Blueprint] = options.pop("urls")
        for rule in urls:
            rule.config = url_config
            rule.mirror = urls
            rule.system = url_system
            rule.enable()
            super().register_blueprint(rule, url_prefix=url_prefix)
        super().run(**options)
