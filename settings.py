import typing

settings: typing.Dict[str, typing.Dict[str, typing.Union[bool, int, str]]] = {
    "logger": {
        "folder": "out/logger"
    },
    "submit": {
        "folder": "out/submit"
    },
    "upload": {
        "folder": "out/upload"
    },
    "wsdl": {
        "debug": False,
        "host": "0.0.0.0",
        "port": 5000,
    }
}
