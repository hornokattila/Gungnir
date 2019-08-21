import os
import typing

settings: typing.Dict[str, typing.Dict[str, typing.Union[bool, int, str]]] = {
    "urls": {
        "logger_folder": os.path.abspath("out/logger"),
        "submit_folder": os.path.abspath("out/submit"),
        "upload_folder": os.path.abspath("out/upload")
    },
    "wsdl": {
        "debug": True,
        "host": "0.0.0.0",
        "port": 5000
    }
}
