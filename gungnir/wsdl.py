import typing

import flask

from gungnir.utils.Blueprint import Blueprint


class Flask(flask.Flask):
    def run(self, **options: typing.Union[str, typing.Dict[str, typing.Union[bool, int, str]], typing.List[Blueprint]]) -> None:
        prints: typing.List[Blueprint] = options.pop("prints")
        prints_config: typing.Dict[str, typing.Union[bool, int, str]] = options.pop("prints_config")
        prints_prefix: str = options.pop("prints_prefix")
        prints_system: typing.Dict[str, typing.Union[bool, int, str]] = options.pop("prints_system")
        for rule in prints:
            rule.config = prints_config
            rule.mirror = prints
            rule.system = prints_system
            rule.enable()
            super().register_blueprint(rule, url_prefix=prints_prefix)
        super().run(**options)
