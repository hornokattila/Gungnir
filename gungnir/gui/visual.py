import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Visual(Blueprint):
    def enable(self) -> None:
        pass

    def detail(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {
            "detail": {"rule": "/detail", "methods": ["GET"]},
            "visual": {"rule": "/", "methods": ["GET"]}
        }


visual: Visual = Visual(LoginManager().vacant_loader)


@visual.route(**visual.detail()["detail"])
def get_detail() -> str:
    detail: typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]] = {}
    for rule in visual.mirror:
        detail.update(rule.detail())
    return visual.flask.json.dumps(detail)


@visual.route(**visual.detail()["visual"])
def get_visual() -> str:
    return visual.flask.render_template("visual.html", detail=get_detail())
