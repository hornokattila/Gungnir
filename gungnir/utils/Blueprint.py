import abc
import typing
from concurrent.futures.thread import ThreadPoolExecutor

import flask
import werkzeug

import settings


class Blueprint(abc.ABC, flask.Blueprint):
    executor: ThreadPoolExecutor = ThreadPoolExecutor(1)

    def __init__(self, name: str, import_name: str) -> None:
        super().__init__(name, import_name)
        self.before_request(self.check_password)
        self.flask: flask = flask
        self.settings: typing.Dict[str, typing.Union[bool, int, str]] = settings.settings["urls"]
        self.werkzeug: werkzeug = werkzeug
        self.init()

    @abc.abstractmethod
    def init(self) -> None:
        pass

    def check_password(self) -> None:
        pass
