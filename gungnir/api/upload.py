import os
import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Upload(Blueprint):
    def init(self) -> None:
        os.makedirs(self.config["upload_folder"], exist_ok=True)

    def spec(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {
            "_upload": {"rule": "/upload", "methods": ["POST"]},
            "_uploads": {"rule": "/uploads", "methods": ["GET"]}
        }


upload: Upload = Upload(LoginManager().kernel_loader)


@upload.route(**upload.spec()["_upload"])
def _upload() -> str:
    uploads: typing.List[str] = []
    for file in upload.flask.request.files:
        name: str = upload.werkzeug.utils.secure_filename(file)
        path: str = os.path.join(upload.config["upload_folder"], name)
        if not os.path.isfile(path):
            upload.flask.request.files[name].save(path)
            uploads.append(name)
    return upload.flask.json.dumps(uploads)


@upload.route(**upload.spec()["_uploads"])
def _uploads() -> str:
    uploads: typing.Dict[str, typing.Dict[str, int]] = {}
    for file in os.scandir(upload.config["upload_folder"]):
        uploads[file.name] = dict(zip(("mode", "ino", "dev", "nlink", "uid", "gid", "size", "atime", "mtime", "ctime"), file.stat()))
    return upload.flask.json.dumps(uploads)
