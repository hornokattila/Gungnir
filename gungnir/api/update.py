import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Update(Blueprint):
    def enable(self) -> None:
        pass

    def detail(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {
            "_system": {"rule": "/system", "methods": ["GET"]},
            "_update": {"rule": "/update", "methods": ["POST"]}
        }


update: Update = Update(LoginManager().shadow_loader)


@update.route(**update.detail()["_system"])
def _get_system() -> str:
    return update.flask.json.dumps(update.system)


@update.route(**update.detail()["_update"])
def _set_update() -> str:
    raise NotImplementedError()
