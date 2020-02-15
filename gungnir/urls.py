import typing

from gungnir.api.deploy import deploy
from gungnir.api.device import device
from gungnir.api.folder import folder
from gungnir.api.system import system
from gungnir.utils.Blueprint import Blueprint

urls: typing.List[Blueprint] = [
    deploy,
    device,
    folder,
    system
]

urls_prefix: str = "/api"
