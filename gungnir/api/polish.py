from services.Housekeeper import Housekeeper
from utils.Blueprint import Blueprint
from utils.LoginManager import LoginManager


class Polish(Blueprint):
    def init(self) -> None:
        pass


polish: Polish = Polish(LoginManager().ba_spwd)


@polish.route("/polish", methods=["POST"])
def _polish() -> str:
    return polish.flask.json.dumps(Housekeeper(
        polish.settings["submit_folder"],
        polish.settings["submit_folder"]).polish(polish.flask.request.json))


@polish.route("/reboot", methods=["POST"])
def _reboot() -> str:
    raise NotImplementedError()
