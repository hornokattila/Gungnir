import flask

health = flask.Blueprint("health", __name__)


@health.route("/health")
def _health() -> str:
    return ""
