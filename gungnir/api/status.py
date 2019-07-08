from utils.Blueprint import Blueprint


class Status(Blueprint):
    def init(self) -> None:
        pass


status: Status = Status("status", __name__)


@status.route("/status")
def _status() -> str:
    return ""
