import os
import typing

settings: typing.Dict[str, typing.Dict[str, typing.Union[bool, int, str]]] = {
    "folder": {
        "deploy": os.path.abspath("out/submit"),
        "logger": os.path.abspath("out/logger"),
        "upload": os.path.abspath("out/upload")
    },
    "server": {
        "host": "0.0.0.0",
        "port": 443,
        "ssl_context": "adhoc"
    },
    "system": {
        "name": "Gungnir",
        "version": "1.0.0"
    }
}
