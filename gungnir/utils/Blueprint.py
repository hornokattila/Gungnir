import abc
import typing

import flask
import werkzeug

import settings


class Blueprint(abc.ABC, flask.Blueprint):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__, self.__class__.__module__)
        self.before_request(self.check_password)
        self.flask: flask = flask
        self.settings: typing.Dict[str, typing.Union[bool, int, str]] = settings.settings["urls"]
        self.werkzeug: werkzeug = werkzeug
        self.init()

    def check_password(self) -> None:
        pass

    @abc.abstractmethod
    def init(self) -> None:
        pass
