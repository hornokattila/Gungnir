import os

from services.Executor import Executor
from utils.Blueprint import Blueprint
from utils.LoginManager import LoginManager


class Submit(Blueprint):
    def init(self) -> None:
        pass


submit: Submit = Submit(LoginManager.header_loader)


@submit.route("/status")
def _status() -> str:
    if os.path.isdir(submit.settings["submit_folder"]):
        return submit.flask.json.dumps(os.listdir(submit.settings["submit_folder"]))
    return ""


@submit.route("/submit", methods=["POST"])
def _submit() -> str:
    return Executor(
        submit.settings["logger_folder"],
        submit.settings["submit_folder"],
        submit.settings["upload_folder"]).submit(submit.flask.request.json)
