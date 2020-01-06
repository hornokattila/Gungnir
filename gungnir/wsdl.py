import typing

import flask

from gungnir.utils.Blueprint import Blueprint


class Flask(flask.Flask):
    def run(self, **options: typing.Union[str, typing.Dict[str, typing.Union[bool, int, str]], typing.List[Blueprint]]) -> None:
        urls: typing.List[Blueprint] = options.pop("urls")
        urls_config: typing.Dict[str, typing.Union[bool, int, str]] = options.pop("urls_config")
        urls_prefix: str = options.pop("urls_prefix")
        urls_system: typing.Dict[str, typing.Union[bool, int, str]] = options.pop("urls_system")
        for rule in urls:
            rule.config = urls_config
            rule.mirror = urls
            rule.system = urls_system
            rule.enable()
            super().register_blueprint(rule, url_prefix=urls_prefix)
        super().run(**options)
