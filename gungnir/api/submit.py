import os
import uuid

from utils.Blueprint import Blueprint
from utils.LoginManager import LoginManager
from utils.ThreadPool import ThreadPool


class Submit(Blueprint):
    def init(self) -> None:
        os.makedirs(self.settings["submit_folder"], exist_ok=True)


submit: Submit = Submit(LoginManager().user_loader)


@submit.route("/status")
def _status() -> str:
    if os.path.isdir(submit.settings["submit_folder"]):
        return submit.flask.json.dumps(os.listdir(submit.settings["submit_folder"]))
    return ""


@submit.route("/submit", methods=["POST"])
def _submit() -> str:
    try:
        ThreadPool.validate(submit.flask.request.json, ["script"])
        name: str = uuid.uuid4().get_hex()
        path: str = os.path.join(submit.settings["submit_folder"], "{0}.bat".format(name))
        with open(path, "x") as file:
            file.write(submit.flask.request.json["script"])
        ThreadPool.submit(os.system, "{0} {1} > {2}".format(path, submit.settings["upload_folder"], os.path.join(submit.settings["logger_folder"], "{0}.log".format(name))))
        ThreadPool.submit(os.remove, path)
        return submit.flask.json.dumps([name])
    except OSError:
        pass
    return ""
