import os
import typing

from util.Blueprint import Blueprint


class Upload(Blueprint):
    def init(self) -> None:
        if not os.path.isdir(self.settings["folder"]):
            os.makedirs(self.settings["folder"])


upload: Upload = Upload("upload", __name__)


@upload.route("/uploads")
def _uploads() -> str:
    return upload.flask.json.dumps(os.listdir(upload.settings["folder"]))


@upload.route("/upload", methods=["POST"])
def _upload() -> str:
    results: typing.List[str] = []
    for filename in upload.flask.request.files:
        path: str = os.path.join(upload.settings["folder"], filename)
        if not os.path.isfile(path):
            upload.flask.request.files[filename].save(path)
            results.append(filename)
    return upload.flask.json.dumps(results)
