import os
import typing
import uuid

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.Environment import Environment
from gungnir.utils.LoginManager import LoginManager
from gungnir.utils.ThreadPool import ThreadPool


class Deploy(Blueprint):
    def detail(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {
            "_deploy": {"rule": "/deploy", "methods": ["POST"]},
            "_reboot": {"rule": "/reboot", "methods": ["POST"]}
        }

    def enable(self) -> None:
        pass


deploy: Deploy = Deploy(LoginManager().shadow_loader)


@deploy.route(**deploy.detail()["_deploy"])
def _deploy() -> str:
    ThreadPool.verify(deploy.flask.request.json, ["script"])
    name: str = uuid.uuid4().hex
    path: str = os.path.join(deploy.folder["deploy"], "{0}.bat".format(name))
    with open(path, "x") as file:
        file.write(deploy.flask.request.json["script"])
    ThreadPool.submit(os.system, "{0} {1} {2} > {3}".format(Environment.RUNNER.decode(), path, deploy.folder["upload"], os.path.join(deploy.folder["logger"], "{0}.log".format(name))))
    ThreadPool.submit(os.remove, path)
    return name


@deploy.route(**deploy.detail()["_reboot"])
def _reboot() -> str:
    ThreadPool.submit(os.system, Environment.REBOOT.decode())
    return ""
