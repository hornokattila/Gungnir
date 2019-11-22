import os
import typing

from utils.Blueprint import Blueprint
from utils.LoginManager import LoginManager


class Upload(Blueprint):
    def init(self) -> None:
        os.makedirs(self.settings["upload_folder"], exist_ok=True)


upload: Upload = Upload(LoginManager().user_loader)


@upload.route("/upload", methods=["POST"])
def _upload() -> str:
    uploads: typing.List[str] = []
    for file in upload.flask.request.files:
        name: str = upload.werkzeug.utils.secure_filename(file)
        path: str = os.path.join(upload.settings["upload_folder"], name)
        if not os.path.isfile(path):
            upload.flask.request.files[name].save(path)
            uploads.append(name)
    return upload.flask.json.dumps(uploads)


@upload.route("/uploads")
def _uploads() -> str:
    uploads: typing.Dict[str, typing.Dict[str, int]] = {}
    for file in os.scandir(upload.settings["upload_folder"]):
        uploads[file.name] = dict(zip(("mode", "ino", "dev", "nlink", "uid", "gid", "size", "atime", "mtime", "ctime"), file.stat()))
    return upload.flask.json.dumps(uploads)
