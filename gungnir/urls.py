import typing

from api.health import health
from api.logger import logger
from utils.Blueprint import Blueprint

version: str = "/v1"
urls: typing.List[Blueprint] = [
    health,
    logger
]
