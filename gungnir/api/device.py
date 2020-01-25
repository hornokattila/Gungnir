import os
import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Device(Blueprint):
    def detail(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {
            "_device": {"rule": "/device", "methods": ["GET"]},
            "_health": {"rule": "/health", "methods": ["GET"]}
        }

    def enable(self) -> None:
        pass


device: Device = Device(LoginManager().shadow_loader)


@device.route(**device.detail()["_device"])
def _get_device() -> str:
    return device.flask.json.dumps(dict(zip(("sysname", "nodename", "release", "version", "machine"), os.uname())))


@device.route(**device.detail()["_health"])
def _get_health() -> str:
    return ""
