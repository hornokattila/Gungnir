import typing

import flask

from api.health import health
from api.logger import logger

version: str = "/v1"
urls: typing.List[flask.Blueprint] = [
    health,
    logger
]
