import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Update(Blueprint):
    def enable(self) -> None:
        pass

    def detail(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {
            "_detail": {"rule": "/detail", "methods": ["GET"]},
            "_system": {"rule": "/system", "methods": ["GET"]}
        }


update: Update = Update(LoginManager().shadow_loader)


@update.route(**update.detail()["_detail"])
def _get_detail() -> str:
    detail: typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]] = {}
    for rule in update.mirror:
        detail.update(rule.detail())
    return update.flask.json.dumps(detail)


@update.route(**update.detail()["_system"])
def _get_system() -> str:
    return update.flask.json.dumps(update.system)
