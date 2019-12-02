import os
import typing

settings: typing.Dict[str, typing.Dict[str, typing.Union[bool, int, str]]] = {
    "pypi": {
        "version": "1.0.0"
    },
    "urls": {
        "logger_folder": os.path.abspath("out/logger"),
        "submit_folder": os.path.abspath("out/submit"),
        "upload_folder": os.path.abspath("out/upload")
    },
    "wsdl": {
        "debug": False,
        "host": "0.0.0.0",
        "port": 443,
        "ssl_context": "adhoc",
        "threaded": True
    }
}
