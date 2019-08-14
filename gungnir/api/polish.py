from services.Housekeeper import Housekeeper
from utils.Whiteprint import Whiteprint


class Polish(Whiteprint):
    pass


polish: Polish = Polish("polish", __name__)


@polish.route("/polish", methods=["POST"])
def _polish() -> str:
    return polish.flask.json.dumps(Housekeeper(
        polish.executor,
        polish.settings["submit"]["folder"],
        polish.settings["upload"]["folder"]).polish(polish.flask.request.json))
