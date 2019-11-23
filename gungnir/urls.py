import typing

from api.health import health
from api.logger import logger
from api.reboot import reboot
from api.submit import submit
from api.update import update
from api.upload import upload
from utils.Blueprint import Blueprint

url_prefix: str = "/api"
urls: typing.List[Blueprint] = [
    health,
    logger,
    reboot,
    submit,
    update,
    upload
]
