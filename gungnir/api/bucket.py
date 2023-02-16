import os
import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Bucket(Blueprint):
    def detail(self) -> typing.List[typing.Dict[str, typing.Union[str, typing.Callable[[], str], typing.List[str]]]]:
        return [
            {"rule": "/bucket/<folder>/<file>", "endpoint": "_delete_file", "view_func": _delete_file, "methods": ["DELETE"]},
            {"rule": "/bucket/<folder>/<file>", "endpoint": "_file", "view_func": _file, "methods": ["GET"]},
            {"rule": "/bucket/<folder>/<file>", "endpoint": "_put_file", "view_func": _put_file, "methods": ["PUT"]},
            {"rule": "/bucket/<folder>", "endpoint": "_files", "view_func": _files, "methods": ["GET"]}
        ]


bucket: Bucket = Bucket(LoginManager().shadow_loader)


def _delete_file(folder: str, file: str) -> str:
    os.remove(os.path.join(bucket.config["bucket"], folder, file))
    return ""


def _file(folder: str, file: str) -> str:
    return bucket.flask.send_from_directory(os.path.join(bucket.config["bucket"], folder), file)


def _put_file(folder: str, file: str) -> str:
    path: str = os.path.join(bucket.config["bucket"], folder, bucket.werkzeug.utils.secure_filename(file))
    with open(path, "wb") as file:
        file.write(bucket.flask.request.data)
    return ""


def _files(folder: str) -> str:
    result: typing.Dict[str, typing.Dict[str, int]] = {}
    for file in os.scandir(os.path.join(bucket.config["bucket"], folder)):
        result[file.name] = dict(zip(("mode", "ino", "dev", "nlink", "uid", "gid", "size", "atime", "mtime", "ctime"), file.stat()))
    return bucket.flask.json.dumps(result)
