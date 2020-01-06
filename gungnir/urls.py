import typing

from gungnir.api.deploy import deploy
from gungnir.api.health import health
from gungnir.api.logger import logger
from gungnir.api.reboot import reboot
from gungnir.api.update import update
from gungnir.api.upload import upload
from gungnir.gui.visual import visual
from gungnir.utils.Blueprint import Blueprint

urls: typing.List[Blueprint] = [
    deploy,
    health,
    logger,
    reboot,
    update,
    upload,
    visual
]

urls_prefix: str = "/api"
