import typing

import flask

from gungnir.utils.Blueprint import Blueprint


class Flask(flask.Flask):
    def run(self: typing.Self, **settings: typing.Union[typing.Dict[str, typing.Dict[str, typing.Union[int, str, typing.Tuple[str, str]]]], typing.Dict[typing.Type[Exception], typing.Callable[[Exception], typing.Tuple[str, int]]], typing.List[Blueprint], str]) -> None:
        errors: typing.Dict[typing.Type[Exception], typing.Callable[[Exception], typing.Tuple[str, int]]] = settings["errors"]
        for rule, config in errors.items():
            super().register_error_handler(rule, config)
        for rule in settings["urls"]:
            rule.config = settings["config"]
            rule.system = settings["system"]
            for detail in rule.details():
                rule.add_url_rule(**detail)
            super().register_blueprint(rule, url_prefix=settings["url_prefix"])
        super().run(**settings["server"])
