import os
import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager
from gungnir.utils.ThreadPool import ThreadPool


class Reboot(Blueprint):
    def init(self) -> None:
        pass

    def spec(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {
            "_reboot": {"rule": "/reboot", "methods": ["POST"]},
            "_remove": {"rule": "/remove", "methods": ["POST"]}
        }


reboot: Reboot = Reboot(LoginManager().kernel_loader)


@reboot.route(**reboot.spec()["_reboot"])
def _reboot() -> str:
    raise NotImplementedError()


@reboot.route(**reboot.spec()["_remove"])
def _remove() -> str:
    uploads: typing.List[str] = []
    ThreadPool.validate(reboot.flask.request.json, ["max_size"])
    for file in os.scandir(reboot.config["upload_folder"]):
        if file.stat().st_size.__gt__(reboot.flask.request.json["max_size"]):
            name: str = file.name
            ThreadPool.submit(os.remove, os.path.join(reboot.config["upload_folder"], name))
            uploads.append(name)
    return reboot.flask.json.dumps(uploads)
