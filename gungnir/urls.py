import typing

from gungnir.api.health import health
from gungnir.api.logger import logger
from gungnir.api.reboot import reboot
from gungnir.api.submit import submit
from gungnir.api.update import update
from gungnir.api.upload import upload
from gungnir.gui.visual import visual
from gungnir.utils.Blueprint import Blueprint

url_prefix: str = "/api"
urls: typing.List[Blueprint] = [
    health,
    logger,
    reboot,
    submit,
    update,
    upload,
    visual
]
