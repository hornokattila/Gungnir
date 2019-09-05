from services.Housekeeper import Housekeeper
from utils.Blueprint import Blueprint
from utils.LoginManager import LoginManager
from utils.ThreadPool import ThreadPool


class Polish(Blueprint, ThreadPool):
    def init(self) -> None:
        pass


polish: Polish = Polish(LoginManager.header_loader)


@polish.route("/polish", methods=["POST"])
def _polish() -> str:
    return polish.flask.json.dumps(Housekeeper(
        polish.executor,
        polish.settings["submit_folder"],
        polish.settings["submit_folder"]).polish(polish.flask.request.json))
