import logging
import os
import typing
from logging import handlers


class Logger:
    config: typing.Dict[str, typing.Union[int, str, typing.Dict[str, typing.Union[int, str]]]] = {}

    def __init__(self: typing.Self, settings: typing.Dict[str, typing.Union[int, str]]) -> None:
        Logger.config.update(settings)
        os.makedirs(os.path.dirname(Logger.config["handler"]["filename"]), exist_ok=True)
        self.handler: logging.FileHandler = handlers.TimedRotatingFileHandler(**Logger.config["handler"])
        self.handler.setFormatter(logging.Formatter(Logger.config["format"]))

    def basic_config(self: typing.Self, logger: logging.Logger) -> None:
        logger.addHandler(self.handler)
        logger.setLevel(Logger.config["level"])

    def get_logger(self: typing.Self, name: str) -> logging.Logger:
        logger: logging.Logger = logging.getLogger(name)
        self.basic_config(logger)
        return logger
