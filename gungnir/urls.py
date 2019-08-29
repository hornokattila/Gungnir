import typing

from api.health import health
from api.logger import logger
from api.polish import polish
from api.submit import submit
from api.upload import upload
from utils.Blueprint import Blueprint

version: str = "/api"
urls: typing.List[Blueprint] = [
    health,
    logger,
    polish,
    submit,
    upload
]
