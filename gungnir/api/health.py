from utils.Blueprint import Blueprint


class Health(Blueprint):
    def init(self) -> None:
        pass


health: Health = Health("health", __name__)


@health.route("/health")
def _health() -> str:
    return ""
