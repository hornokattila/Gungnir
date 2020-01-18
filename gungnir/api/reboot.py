import os
import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager
from gungnir.utils.ThreadPool import ThreadPool


class Reboot(Blueprint):
    def enable(self) -> None:
        pass

    def detail(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {
            "_reboot": {"rule": "/reboot", "methods": ["POST"]},
            "_remove": {"rule": "/remove", "methods": ["POST"]}
        }


reboot: Reboot = Reboot(LoginManager().shadow_loader)


@reboot.route(**reboot.detail()["_reboot"])
def _set_reboot() -> str:
    volume: typing.Dict[str, int] = {"volume": ThreadPool.volume()}
    ThreadPool.finish()
    return reboot.flask.json.dumps(volume)


@reboot.route(**reboot.detail()["_remove"])
def _set_remove() -> str:
    uploads: typing.List[str] = []
    ThreadPool.verify(reboot.flask.request.json, ["max_size"])
    for file in os.scandir(reboot.config["upload_folder"]):
        if file.stat().st_size.__gt__(reboot.flask.request.json["max_size"]):
            name: str = file.name
            ThreadPool.submit(os.remove, os.path.join(reboot.config["upload_folder"], name))
            uploads.append(name)
    return reboot.flask.json.dumps(uploads)
