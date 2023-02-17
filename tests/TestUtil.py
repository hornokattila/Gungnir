from gungnir.utils.Blueprint import Blueprint


class TestUtil:
    @staticmethod
    def view_func(blueprint: Blueprint, rule: str, *args) -> str:
        for detail in blueprint.detail():
            if detail["rule"] == rule:
                return detail["view_func"](*args)
