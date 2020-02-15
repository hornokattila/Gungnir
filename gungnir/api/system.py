import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class System(Blueprint):
    def detail(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {
            "_detail": {"rule": "/detail", "methods": ["GET"]},
            "_system": {"rule": "/system", "methods": ["GET"]}
        }

    def enable(self) -> None:
        pass


system: System = System(LoginManager().shadow_loader)


@system.route(**system.detail()["_detail"])
def _detail() -> str:
    detail: typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]] = {}
    for rule in system.mirror:
        detail.update(rule.detail())
    return system.flask.json.dumps(detail)


@system.route(**system.detail()["_system"])
def _system() -> str:
    return system.flask.json.dumps(system.system)
