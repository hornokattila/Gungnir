import os
import typing
import uuid

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager
from gungnir.utils.ThreadPool import ThreadPool


class Submit(Blueprint):
    def init(self) -> None:
        os.makedirs(self.config["submit_folder"], exist_ok=True)

    def spec(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {
            "_status": {"rule": "/status", "methods": ["GET"]},
            "_submit": {"rule": "/submit", "methods": ["POST"]}
        }


submit: Submit = Submit(LoginManager().system_loader)


@submit.route(**submit.spec()["_status"])
def _status() -> str:
    return submit.flask.json.dumps(os.listdir(submit.config["submit_folder"]))


@submit.route(**submit.spec()["_submit"])
def _submit() -> str:
    ThreadPool.validate(submit.flask.request.json, ["script"])
    name: str = uuid.uuid4().get_hex()
    path: str = os.path.join(submit.config["submit_folder"], "{0}.bat".format(name))
    with open(path, "x") as file:
        file.write(submit.flask.request.json["script"])
    ThreadPool.submit(os.system, "{0} {1} > {2}".format(path, submit.config["upload_folder"], os.path.join(submit.config["logger_folder"], "{0}.log".format(name))))
    ThreadPool.submit(os.remove, path)
    return submit.flask.json.dumps([name])
