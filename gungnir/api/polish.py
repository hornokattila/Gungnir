from services.Housekeeper import Housekeeper
from utils.Blueprint import Blueprint


class Polish(Blueprint):
    def init(self) -> None:
        pass


polish: Polish = Polish("polish", __name__)


@polish.route("/polish", methods=["POST"])
def _polish() -> str:
    return polish.flask.json.dumps(Housekeeper(
        polish.executor,
        polish.settings["submit_folder"],
        polish.settings["submit_folder"]).polish(polish.flask.request.json))
