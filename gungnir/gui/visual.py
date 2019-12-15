import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Visual(Blueprint):
    def init(self) -> None:
        pass

    def spec(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {"_visual": {"rule": "/", "methods": ["GET"]}}


visual: Visual = Visual(LoginManager().vacant_loader)


@visual.route(**visual.spec()["_visual"])
def _visual() -> str:
    return visual.flask.render_template("visual.html", **visual.system)
