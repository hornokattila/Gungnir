import os

from utils.Blueprint import Blueprint
from utils.LoginManager import LoginManager


class Logger(Blueprint):
    def init(self) -> None:
        if not os.path.isdir(self.settings["logger_folder"]):
            os.makedirs(self.settings["logger_folder"])


logger: Logger = Logger(LoginManager.header_loader)


@logger.route("/logger/<path:file>")
def _logger(file: str) -> str:
    return logger.flask.send_from_directory(logger.settings["logger_folder"], file)


@logger.route("/loggers")
def _loggers() -> str:
    return logger.flask.json.dumps(os.listdir(logger.settings["logger_folder"]))
