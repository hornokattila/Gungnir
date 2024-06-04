import logging
import os
import typing
from logging.handlers import TimedRotatingFileHandler


class LogHandler:
    config: typing.Dict[str, typing.Union[int, str, typing.Dict[str, typing.Union[int, str]]]] = {}

    def __init__(self: typing.Self, settings: typing.Dict[str, typing.Union[int, str]]) -> None:
        LogHandler.config.update(settings)
        os.makedirs(os.path.dirname(LogHandler.config["handler"]["filename"]), exist_ok=True)
        self.handler: logging.FileHandler = TimedRotatingFileHandler(**LogHandler.config["handler"])
        self.handler.setFormatter(logging.Formatter(LogHandler.config["format"]))

    def basic_config(self: typing.Self, logger: logging.Logger) -> None:
        logger.addHandler(self.handler)
        logger.setLevel(LogHandler.config["level"])

    def get_logger(self: typing.Self, name: str) -> logging.Logger:
        logger: logging.Logger = logging.getLogger(name)
        self.basic_config(logger)
        return logger
