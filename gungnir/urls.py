import typing

from gungnir.api.deploy import deploy
from gungnir.api.device import device
from gungnir.api.logger import logger
from gungnir.api.reboot import reboot
from gungnir.api.system import system
from gungnir.api.upload import upload
from gungnir.utils.Blueprint import Blueprint

urls: typing.List[Blueprint] = [
    deploy,
    device,
    logger,
    reboot,
    system,
    upload
]

urls_prefix: str = "/api"
