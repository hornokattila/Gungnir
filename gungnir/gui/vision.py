from utils.Blueprint import Blueprint
from utils.LoginManager import LoginManager


class Vision(Blueprint):
    def init(self) -> None:
        pass


vision: Vision = Vision(LoginManager().void_loader)


@vision.route("/vision")
def _vision() -> str:
    raise NotImplementedError()
