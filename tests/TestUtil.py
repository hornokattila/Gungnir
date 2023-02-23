from gungnir.utils.Blueprint import Blueprint


class TestUtil:
    @staticmethod
    def view_func(blueprint: Blueprint, rule: str, method: str, *args: ...) -> str:
        for detail in blueprint.detail():
            if rule == detail["rule"] and method in detail["methods"]:
                return detail["view_func"](*args)
