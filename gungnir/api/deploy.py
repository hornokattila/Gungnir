import os
import typing
import uuid

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.Environment import Environment
from gungnir.utils.LoginManager import LoginManager
from gungnir.utils.ThreadPool import ThreadPool


class Deploy(Blueprint):
    def detail(self) -> typing.List[typing.Dict[str, typing.Union[str, typing.Callable[..., str], typing.List[str]]]]:
        return [
            {"rule": "/deploy", "endpoint": "_deploy", "view_func": _deploy, "methods": ["POST"]},
            {"rule": "/reboot", "endpoint": "_reboot", "view_func": _reboot, "methods": ["POST"]}
        ]


deploy: Deploy = Deploy(LoginManager().shadow_loader)


def _deploy() -> str:
    ThreadPool.verify(deploy.flask.request.json, ["script"])
    name: str = uuid.uuid4().hex
    path: str = os.path.join(deploy.config["folder"], "deploy", name)
    with open(path, "x") as file:
        file.write(deploy.flask.request.json["script"])
    ThreadPool.submit(os.system, "{0} {1} {2} > {3}".format(Environment.RUNNER.decode(), path, os.path.join(deploy.config["folder"], "upload"), os.path.join(deploy.config["folder"], "logger", name)))
    ThreadPool.submit(os.remove, path)
    return name


def _reboot() -> str:
    os.system(Environment.REBOOT.decode())
    return ""
