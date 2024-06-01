import os
import typing
import uuid

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager
from gungnir.utils.ThreadPool import ThreadPool


class Deploy(Blueprint):
    def details(self: typing.Self) -> typing.List[typing.Dict[str, typing.Union[str, typing.Callable[..., str], typing.List[str]]]]:
        return [{"rule": "/deploy", "endpoint": "_put_script", "view_func": _put_script, "methods": ["PUT"]}]

    @staticmethod
    def initialize() -> str:
        for folder in ["deploy", "logger", "upload"]:
            os.makedirs(os.path.join(deploy.config["bucket"], folder), exist_ok=True)
        return uuid.uuid4().hex


deploy: Deploy = Deploy(LoginManager().shadow_loader)


def _put_script() -> str:
    name: str = deploy.initialize()
    def _path_finder(folder: str) -> str: return os.path.join(deploy.config["bucket"], folder)
    def _file_finder(folder: str) -> str: return os.path.join(_path_finder(folder), name)
    file: str = _file_finder("deploy")
    with open(file, "wb") as script:
        script.write(deploy.flask.request.data)
    ThreadPool.submit(file, _path_finder("upload"), _file_finder("logger"))
    return name
