import typing

from api.health import health
from api.logger import logger
from api.upload import upload
from util.Blueprint import Blueprint

version: str = "/v1"
urls: typing.List[Blueprint] = [
    health,
    logger,
    upload
]
