import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Update(Blueprint):
    def init(self) -> None:
        pass

    def spec(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {
            "_update": {"rule": "/update", "methods": ["POST"]},
            "_version": {"rule": "/version", "methods": ["GET"]}
        }


update: Update = Update(LoginManager().kernel_loader)


@update.route(**update.spec()["_update"])
def _update() -> str:
    raise NotImplementedError()


@update.route(**update.spec()["_version"])
def _version() -> str:
    raise NotImplementedError()
