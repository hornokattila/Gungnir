import logging
import os
import typing
from logging.handlers import TimedRotatingFileHandler


class LogHandler:
    # TODO: FIXME!
    def __init__(self: typing.Self, settings: typing.Dict[str, typing.Union[int, str, typing.Dict[str, typing.Union[int, str]]]]) -> None:
        os.makedirs(os.path.dirname(settings["handler"]["filename"]), exist_ok=True)
        self.handler = TimedRotatingFileHandler(**settings["handler"])
        self.handler.setFormatter(logging.Formatter(settings["format"]))
        self.handler.setLevel(settings["level"])

    def get_logger(self: typing.Self, name: str) -> logging.Logger:
        logger: logging.Logger = logging.getLogger(name)
        logger.addHandler(self.handler)
        logger.setLevel(self.handler.level)
        return logger
