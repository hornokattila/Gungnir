import os
import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Bucket(Blueprint):
    def detail(self) -> typing.List[typing.Dict[str, typing.Union[str, typing.Callable[..., str], typing.List[str]]]]:
        return [
            {"rule": "/bucket/<folder>/<file>", "endpoint": "_delete_file", "view_func": _delete_file, "methods": ["DELETE"]},
            {"rule": "/bucket/<folder>/<file>", "endpoint": "_file", "view_func": _file, "methods": ["GET"]},
            {"rule": "/bucket/<folder>", "endpoint": "_files", "view_func": _files, "methods": ["GET"]},
            {"rule": "/bucket/<folder>", "endpoint": "_post_file", "view_func": _post_file, "methods": ["POST"]}
        ]


bucket: Bucket = Bucket(LoginManager().shadow_loader)


def _delete_file(folder: str, file: str) -> str:
    os.remove(os.path.join(bucket.config["bucket"], folder, file))
    return ""


def _file(folder: str, file: str) -> str:
    return bucket.flask.send_from_directory(os.path.join(bucket.config["bucket"], folder), file)


def _files(folder: str) -> str:
    result: typing.Dict[str, typing.Dict[str, int]] = {}
    for file in os.scandir(os.path.join(bucket.config["bucket"], folder)):
        result[file.name] = dict(zip(("mode", "ino", "dev", "nlink", "uid", "gid", "size", "atime", "mtime", "ctime"), file.stat()))
    return bucket.flask.json.dumps(result)


def _post_file(folder: str) -> str:
    for file in bucket.flask.request.files:
        try:
            file.save(os.path.join(bucket.config["bucket"], folder, bucket.werkzeug.utils.secure_filename(file)))
        except FileNotFoundError:
            os.makedirs(os.path.join(bucket.config["bucket"], folder))
            return _post_file(folder)
    return ""
