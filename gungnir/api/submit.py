import os
import uuid

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
    if not os.path.isdir(submit.settings["submit"]["folder"]):
        try:
            os.makedirs(submit.settings["submit"]["folder"])
            name: str = uuid.uuid4().hex
            path: str = os.path.join(submit.settings["submit"]["folder"], name)
            return name
        except OSError:
            pass
    return ""
