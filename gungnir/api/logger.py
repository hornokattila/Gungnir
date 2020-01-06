import os
import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager
from gungnir.utils.ThreadPool import ThreadPool


class Logger(Blueprint):
    def enable(self) -> None:
        os.makedirs(self.config["logger_folder"], exist_ok=True)

    def detail(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {
            "_logger": {"rule": "/logger", "methods": ["GET"]},
            "_loggers": {"rule": "/loggers", "methods": ["GET"]}
        }


logger: Logger = Logger(LoginManager().kernel_loader)


@logger.route(**logger.detail()["_logger"])
def _get_logger() -> str:
    ThreadPool.verify(logger.flask.request.json, ["file"])
    return logger.flask.send_from_directory(logger.config["logger_folder"], logger.flask.request.json["file"])


@logger.route(**logger.detail()["_loggers"])
def _get_loggers() -> str:
    return logger.flask.json.dumps(os.listdir(logger.config["logger_folder"]))
