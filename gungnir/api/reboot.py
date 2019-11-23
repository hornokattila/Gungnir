import os
import typing

from utils.Blueprint import Blueprint
from utils.LoginManager import LoginManager
from utils.ThreadPool import ThreadPool


class Reboot(Blueprint):
    def init(self) -> None:
        pass


reboot: Reboot = Reboot(LoginManager().user_loader)


@reboot.route("/reboot", methods=["POST"])
def _reboot() -> str:
    raise NotImplementedError()


@reboot.route("/remove", methods=["POST"])
def _remove() -> str:
    uploads: typing.List[str] = []
    ThreadPool.validate(reboot.flask.request.json, ["max_size"])
    for file in os.scandir(reboot.settings["upload_folder"]):
        if file.stat().st_size.__gt__(reboot.flask.request.json["max_size"]):
            name: str = file.name
            ThreadPool.submit(os.remove, os.path.join(reboot.settings["upload_folder"], name))
            uploads.append(name)
    return reboot.flask.json.dumps(uploads)
