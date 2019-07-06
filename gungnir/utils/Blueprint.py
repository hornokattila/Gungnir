import abc
import typing

import flask
import werkzeug

import settings


class Blueprint(abc.ABC, flask.Blueprint):
    def __init__(self, name: str, import_name: str) -> None:
        self.flask: flask = flask
        self.werkzeug: werkzeug = werkzeug
        self.settings: typing.Dict[str, typing.Union[bool, int, str]] = {}
        if name in settings.settings:
            self.settings = settings.settings[name]
        super().__init__(name, import_name)
        self.init()

    @abc.abstractmethod
    def init(self) -> None:
        pass
