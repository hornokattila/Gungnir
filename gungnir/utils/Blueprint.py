import abc
import typing

import flask
import werkzeug


class Blueprint(abc.ABC, flask.Blueprint):
    def __init__(self, header_loader: typing.Callable[[typing.Dict[str, str]], None]) -> None:
        super().__init__(self.__class__.__name__, self.__class__.__module__)
        self.before_request(self._request_loader)
        self.config: typing.Dict[str, typing.Union[bool, int, str]] = {}
        self.flask: flask = flask
        self.header_loader: typing.Callable[[typing.Dict[str, str]], None] = header_loader
        self.mirror: typing.List[Blueprint] = []
        self.system: typing.Dict[str, typing.Union[bool, int, str]] = {}
        self.werkzeug: werkzeug = werkzeug

    @abc.abstractmethod
    def detail(self) -> typing.List[typing.Dict[str, typing.Union[str, typing.Callable[..., str], typing.List[str]]]]:
        pass

    def _request_loader(self) -> None:
        self.header_loader(self.flask.request.headers)
