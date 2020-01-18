import os
import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Health(Blueprint):
    def enable(self) -> None:
        pass

    def detail(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {
            "_device": {"rule": "/device", "methods": ["GET"]},
            "_health": {"rule": "/health", "methods": ["GET"]}
        }


health: Health = Health(LoginManager().shadow_loader)


@health.route(**health.detail()["_device"])
def _get_device() -> str:
    return health.flask.json.dumps(dict(zip(("sysname", "nodename", "release", "version", "machine"), os.uname())))


@health.route(**health.detail()["_health"])
def _get_health() -> str:
    return ""
