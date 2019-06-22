import typing

import flask

from api.health import health

version: str = "/v1"
urls: typing.List[flask.Blueprint] = [
    health
]
