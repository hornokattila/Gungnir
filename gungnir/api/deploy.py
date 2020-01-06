import os
import typing
import uuid

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager
from gungnir.utils.ThreadPool import ThreadPool


class Deploy(Blueprint):
    def enable(self) -> None:
        os.makedirs(self.config["submit_folder"], exist_ok=True)

    def detail(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {
            "_deploy": {"rule": "/deploy", "methods": ["POST"]},
            "_status": {"rule": "/status", "methods": ["GET"]}
        }


deploy: Deploy = Deploy(LoginManager().kernel_loader)


@deploy.route(**deploy.detail()["_status"])
def _get_status() -> str:
    return deploy.flask.json.dumps(os.listdir(deploy.config["submit_folder"]))


@deploy.route(**deploy.detail()["_deploy"])
def _set_deploy() -> str:
    ThreadPool.verify(deploy.flask.request.json, ["script"])
    name: str = uuid.uuid4().get_hex()
    path: str = os.path.join(deploy.config["submit_folder"], "{0}.bat".format(name))
    with open(path, "x") as file:
        file.write(deploy.flask.request.json["script"])
    ThreadPool.submit(os.system, "{0} {1} > {2}".format(path, deploy.config["upload_folder"], os.path.join(deploy.config["logger_folder"], "{0}.log".format(name))))
    ThreadPool.submit(os.remove, path)
    return deploy.flask.json.dumps([name])
