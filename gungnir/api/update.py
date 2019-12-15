from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Update(Blueprint):
    def init(self) -> None:
        pass

    def spec(self) -> None:
        pass


update: Update = Update(LoginManager().system_loader)


@update.route("/update", methods=["POST"])
def _update() -> str:
    raise NotImplementedError()


@update.route("/version")
def _version() -> str:
    raise NotImplementedError()
