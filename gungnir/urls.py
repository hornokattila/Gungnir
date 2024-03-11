import typing

from gungnir.api.bucket import bucket
from gungnir.api.deploy import deploy
from gungnir.api.device import device
from gungnir.utils.Blueprint import Blueprint

errors: typing.Dict[typing.Type[Exception], typing.Callable[[Exception], typing.Tuple[str, int]]] = {
    PermissionError: lambda error: ("", 401)
}

urls: typing.List[Blueprint] = [
    bucket,
    deploy,
    device
]

url_prefix: str = "/api"
