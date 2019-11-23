from utils.Blueprint import Blueprint
from utils.LoginManager import LoginManager


class Update(Blueprint):
    def init(self) -> None:
        pass


update: Update = Update(LoginManager().user_loader)


@update.route("/update", methods=["POST"])
def _update() -> str:
    raise NotImplementedError()


@update.route("/version")
def _version() -> str:
    raise NotImplementedError()
