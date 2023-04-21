import typing

from gungnir.utils.Blueprint import Blueprint


class TestUtil:
    @staticmethod
    def view_func(blueprint: Blueprint, rule: str, method: str, *args: str) -> str:
        for detail in blueprint.detail():
            if rule == detail["rule"] and method in detail["methods"]:
                return detail["view_func"](*args)

    @staticmethod
    def catch(method: typing.Callable[[], str]) -> typing.Union[str, typing.Type[Exception]]:
        try:
            return method()
        except Exception as exception:
            return exception.__class__
