import os
import typing

settings: typing.Dict[str, typing.Dict[str, typing.Union[int, str]]] = {
    "config": {
        "bucket": os.path.abspath(".pytest_cache")
    },
    "server": {
        "host": "0.0.0.0",
        "port": 443,
        "ssl_context": "adhoc"
    },
    "system": {
        "groupId": "vaskaktusz",
        "artifactId": "gungnir",
        "version": "1.0.0"
    }
}
