import os
import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Logger(Blueprint):
    def init(self) -> None:
        os.makedirs(self.config["logger_folder"], exist_ok=True)

    def spec(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {
            "_logger": {"rule": "/logger/<path:file>", "methods": ["GET"]},
            "_loggers": {"rule": "/loggers", "methods": ["GET"]}
        }


logger: Logger = Logger(LoginManager().system_loader)


@logger.route(**logger.spec()["_logger"])
def _logger(file: str) -> str:
    return logger.flask.send_from_directory(logger.config["logger_folder"], file)


@logger.route(**logger.spec()["_loggers"])
def _loggers() -> str:
    return logger.flask.json.dumps(os.listdir(logger.config["logger_folder"]))
