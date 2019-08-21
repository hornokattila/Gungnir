import os

from services.Executor import Executor
from utils.Whiteprint import Whiteprint


class Submit(Whiteprint):
    pass


submit: Submit = Submit("submit", __name__)


@submit.route("/status")
def _status() -> str:
    if os.path.isdir(submit.settings["submit_folder"]):
        return submit.flask.json.dumps(os.listdir(submit.settings["submit_folder"]))
    return ""


@submit.route("/submit", methods=["POST"])
def _submit() -> str:
    return Executor(
        submit.executor,
        submit.settings["logger_folder"],
        submit.settings["submit_folder"],
        submit.settings["upload_folder"]).submit(submit.flask.request.json)
