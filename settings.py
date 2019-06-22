import typing

Dict: typing.Type["Dict"] = typing.Dict[str, typing.Union[bool, int, str, typing.Dict[str, typing.Type["Dict"]], typing.List[typing.Type["Dict"]]]]

settings: Dict = {
    "wsdl": {
        "debug": False,
        "host": "0.0.0.0",
        "port": 5000,
    }
}
