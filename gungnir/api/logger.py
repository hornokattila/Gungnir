import os
import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Logger(Blueprint):
    def enable(self) -> None:
        os.makedirs(self.config["logger_folder"], exist_ok=True)

    def detail(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {
            "_logger": {"rule": "/logger/<path:file>", "methods": ["GET"]},
            "_loggers": {"rule": "/loggers", "methods": ["GET"]}
        }


logger: Logger = Logger(LoginManager().kernel_loader)


@logger.route(**logger.detail()["_logger"])
def _get_logger(file: str) -> str:
    return logger.flask.send_from_directory(logger.config["logger_folder"], file)


@logger.route(**logger.detail()["_loggers"])
def _get_loggers() -> str:
    return logger.flask.json.dumps(os.listdir(logger.config["logger_folder"]))
