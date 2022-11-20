import os
import typing

settings: typing.Dict[str, typing.Dict[str, typing.Union[int, str]]] = {
    "config": {
        "bucket": os.environ["BUCKET"]
    },
    "server": {
        "host": "0.0.0.0",
        "port": 443,
        "ssl_context": (os.environ["PUB"], os.environ["KEY"])
    },
    "system": {
        "groupId": "vaskaktusz",
        "artifactId": "gungnir",
        "version": "1.0.0"
    }
}
