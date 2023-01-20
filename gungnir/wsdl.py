import typing

import flask

from gungnir.utils.Blueprint import Blueprint


class Flask(flask.Flask):
    def run(self, **settings: typing.Union[str, typing.Dict[str, typing.Dict[str, typing.Union[int, str, typing.Tuple[str, str]]]], typing.List[Blueprint]]) -> None:
        mirror: typing.List[Blueprint] = settings["urls"]
        for rule in mirror:
            rule.config = settings["config"]
            rule.mirror = mirror
            rule.system = settings["system"]
            rule.launch()
            for detail in rule.detail():
                rule.add_url_rule(**detail)
            super().register_blueprint(rule, url_prefix=settings["url_prefix"])
        super().run(**settings.pop("server"))
