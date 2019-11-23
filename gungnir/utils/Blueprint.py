import abc
import typing

import flask
import werkzeug


class Blueprint(abc.ABC, flask.Blueprint):
    def __init__(self, header_loader: typing.Callable[[typing.Dict[str, str]], None]) -> None:
        super().__init__(self.__class__.__name__, self.__class__.__module__)
        self.before_request(self.request_loader)
        self.flask: flask = flask
        self.header_loader: typing.Callable[[typing.Dict[str, str]], None] = header_loader
        self.settings: typing.Dict[str, typing.Union[bool, int, str]] = {}
        self.werkzeug: werkzeug = werkzeug

    @abc.abstractmethod
    def init(self) -> None:
        pass

    def request_loader(self) -> None:
        self.header_loader(self.flask.request.headers)
