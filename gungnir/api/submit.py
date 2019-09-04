import os

from services.Executor import Executor
from utils.Blueprint import Blueprint
from utils.ThreadPool import ThreadPool


class Submit(Blueprint, ThreadPool):
    def init(self) -> None:
        pass


submit: Submit = Submit()


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
