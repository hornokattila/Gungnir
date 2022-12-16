import os
import typing

settings: typing.Dict[str, typing.Dict[str, typing.Union[int, str]]] = {
    "config": {
        "bucket": os.environ.get("BUCKET", os.path.join(os.path.dirname(__file__), ".pytest_cache"))
    },
    "server": {
        "host": "0.0.0.0",
        "port": 443,
        "ssl_context": (os.environ["PUB"], os.environ["KEY"]) if "PUB" and "KEY" in os.environ else "adhoc"
    },
    "system": {
        "groupId": "vaskaktusz",
        "artifactId": "gungnir",
        "version": "1.0.0"
    }
}
