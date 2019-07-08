from utils.Blueprint import Blueprint


class Submit(Blueprint):
    def init(self) -> None:
        pass


submit: Submit = Submit("submit", __name__)


@submit.route("/submit")
def _submit() -> str:
    return ""
