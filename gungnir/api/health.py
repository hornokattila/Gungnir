import os

from utils.Blueprint import Blueprint
from utils.LoginManager import LoginManager


class Health(Blueprint):
    def init(self) -> None:
        pass


health: Health = Health(LoginManager().system_loader)


@health.route("/health")
def _health() -> str:
    return ""


@health.route("/system")
def _system() -> str:
    return health.flask.json.dumps(dict(zip(("sysname", "nodename", "release", "version", "machine"), os.uname())))
