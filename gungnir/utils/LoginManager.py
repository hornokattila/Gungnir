import abc
import typing


class LoginManager(abc.ABC):
    @staticmethod
    def header_loader(headers: typing.Dict[str, str]) -> None:
        pass
