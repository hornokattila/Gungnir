from utils.Blueprint import Blueprint


class Submit(Blueprint):
    def init(self) -> None:
        pass


submit: Submit = Submit("submit", __name__)


@submit.route("/status")
def _status() -> str:
    return ""


@submit.route("/submit", methods=["POST"])
def _submit() -> str:
    return ""
