import os
import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Health(Blueprint):
    def init(self) -> None:
        pass

    def spec(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {
            "_health": {"rule": "/health", "methods": ["GET"]},
            "_system": {"rule": "/system", "methods": ["GET"]}
        }


health: Health = Health(LoginManager().system_loader)


@health.route(**health.spec()["_health"])
def _health() -> str:
    return ""


@health.route(**health.spec()["_system"])
def _system() -> str:
    return health.flask.json.dumps(dict(zip(("sysname", "nodename", "release", "version", "machine"), os.uname())))
