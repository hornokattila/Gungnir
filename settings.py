import typing

settings: typing.Dict[str, typing.Union[typing.Dict[str, typing.Dict[str, str]], typing.Dict[str, typing.Union[bool, int, str]]]] = {
    "urls": {
        "logger": {
            "folder": "out/logger"
        },
        "polish": {
        },
        "submit": {
            "folder": "out/submit"
        },
        "upload": {
            "folder": "out/upload"
        }
    },
    "wsdl": {
        "debug": True,
        "host": "0.0.0.0",
        "port": 5000,
    }
}
