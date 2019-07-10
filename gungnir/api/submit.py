import os

from services.Executor import Executor
from utils.Blueprint import Blueprint


class Submit(Blueprint):
    def init(self) -> None:
        pass


submit: Submit = Submit("submit", __name__)


@submit.route("/status")
def _status() -> str:
    if os.path.isdir(submit.settings["submit"]["folder"]):
        return submit.flask.json.dumps(os.listdir(submit.settings["submit"]["folder"]))
    return ""


@submit.route("/submit", methods=["POST"])
def _submit() -> str:
    return Executor(submit.settings["logger"]["folder"], submit.settings["submit"]["folder"], submit.settings["upload"]["folder"]).submit(submit.flask.request.json)
