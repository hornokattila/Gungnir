import platform
import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Device(Blueprint):
    def details(self: typing.Self) -> typing.List[typing.Dict[str, typing.Union[str, typing.Callable[..., str], typing.List[str]]]]:
        return [
            {"rule": "/device", "endpoint": "_device", "view_func": _device, "methods": ["GET"]},
            {"rule": "/health", "endpoint": "_health", "view_func": _health, "methods": ["GET"]},
            {"rule": "/system", "endpoint": "_system", "view_func": _system, "methods": ["GET"]}
        ]


device: Device = Device(LoginManager().shadow_loader)


def _device() -> str:
    return device.flask.json.dumps(dict(zip(("system", "node", "release", "version", "machine", "processor"), platform.uname())))


def _health() -> str:
    return ""


def _system() -> str:
    return device.flask.json.dumps(device.system)
