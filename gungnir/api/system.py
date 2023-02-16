import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class System(Blueprint):
    def detail(self) -> typing.List[typing.Dict[str, typing.Union[str, typing.Callable[[], str], typing.List[str]]]]:
        return [
            {"rule": "/detail", "endpoint": "_detail", "view_func": _detail, "methods": ["GET"]},
            {"rule": "/system", "endpoint": "_system", "view_func": _system, "methods": ["GET"]}
        ]


system: System = System(LoginManager().shadow_loader)


def _detail() -> str:
    detail: typing.List[typing.Dict[str, typing.Union[str, typing.List[str]]]] = []
    for rule in system.mirror:
        detail.extend(rule.detail())
    return system.flask.json.dumps(detail, default=lambda object: object.__name__)


def _system() -> str:
    return system.flask.json.dumps(system.system)
