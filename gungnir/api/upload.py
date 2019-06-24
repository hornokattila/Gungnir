import os

from utils.Blueprint import Blueprint


class Upload(Blueprint):
    def init(self) -> None:
        if not os.path.isdir(self.settings["folder"]):
            os.makedirs(self.settings["folder"])


upload: Upload = Upload("upload", __name__)


@upload.route("/uploads")
def _uploads() -> str:
    return upload.flask.json.dumps(os.listdir(upload.settings["folder"]))


@upload.route("/upload")
def _upload() -> str:
    return ""
