import typing

import flask

from gungnir.utils.Blueprint import Blueprint


class Flask(flask.Flask):
    def run(self, **options: typing.Union[str, typing.Dict[str, typing.Union[int, str]], typing.List[Blueprint]]) -> None:
        mirror: typing.List[Blueprint] = options["urls"]
        for rule in mirror:
            rule.config = options["config"]
            rule.mirror = mirror
            rule.system = options["system"]
            rule.launch()
            for detail in rule.detail():
                rule.add_url_rule(**detail)
            super().register_blueprint(rule, url_prefix=options["url_prefix"])
        super().run(**options.pop("server"))
