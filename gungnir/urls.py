import typing

from api.health import health
from api.logger import logger
from api.status import status
from api.submit import submit
from api.upload import upload
from utils.Blueprint import Blueprint

version: str = "/v1"
urls: typing.List[Blueprint] = [
    health,
    logger,
    status,
    submit,
    upload
]
