import os

from utils.Blueprint import Blueprint


class Logger(Blueprint):
    def init(self) -> None:
        if not os.path.isdir(self.settings["folder"]):
            os.makedirs(self.settings["folder"])


logger: Logger = Logger("logger", __name__)


@logger.route("/loggers")
def _loggers() -> str:
    return logger.flask.json.dumps(os.listdir(logger.settings["folder"]))


@logger.route("/logger/<path:file>")
def _logger(file: str) -> str:
    return logger.flask.send_from_directory(logger.settings["folder"], file)
