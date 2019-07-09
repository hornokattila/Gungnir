import os

from utils.Blueprint import Blueprint


class Submit(Blueprint):
    def init(self) -> None:
        pass


submit: Submit = Submit("submit", __name__)


@submit.route("/status")
def _status() -> str:
    if os.path.isdir(submit.settings["folder"]):
        return submit.flask.json.dumps(os.listdir(submit.settings["folder"]))
    return ""


@submit.route("/submit", methods=["POST"])
def _submit() -> str:
    return ""
