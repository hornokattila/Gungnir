from services.Housekeeper import Housekeeper
from utils.Whiteprint import Whiteprint


class Polish(Whiteprint):
    pass


polish: Polish = Polish("polish", __name__)


@polish.route("/polish")
def _polish() -> str:
    return Housekeeper(
        polish.executor,
        polish.settings["submit"]["folder"],
        polish.settings["upload"]["folder"]).attach()
