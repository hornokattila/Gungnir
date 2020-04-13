import typing

from gungnir.api.bucket import bucket
from gungnir.api.deploy import deploy
from gungnir.api.device import device
from gungnir.api.system import system
from gungnir.utils.Blueprint import Blueprint

urls: typing.List[Blueprint] = [
    bucket,
    deploy,
    device,
    system
]

url_prefix: str = "/api"
