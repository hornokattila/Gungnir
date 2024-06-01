import os
import shutil
import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Bucket(Blueprint):
    def details(self: typing.Self) -> typing.List[typing.Dict[str, typing.Union[str, typing.Callable[..., str], typing.List[str]]]]:
        return [
            {"rule": "/bucket/<folder>/<file>", "endpoint": "_delete_file", "view_func": _delete_file, "methods": ["DELETE"]},
            {"rule": "/bucket/<folder>", "endpoint": "_delete_files", "view_func": _delete_files, "methods": ["DELETE"]},
            {"rule": "/bucket/<folder>/<file>", "endpoint": "_file", "view_func": _file, "methods": ["GET"]},
            {"rule": "/bucket/<folder>", "endpoint": "_files", "view_func": _files, "methods": ["GET"]},
            {"rule": "/bucket/<folder>/<file>", "endpoint": "_put_file", "view_func": _put_file, "methods": ["PUT"]}
        ]


bucket: Bucket = Bucket(LoginManager().shadow_loader)


def _delete_file(folder: str, file: str) -> str:
    os.remove(os.path.join(bucket.config["bucket"], folder, file))
    return ""


def _delete_files(folder: str) -> str:
    shutil.rmtree(os.path.join(bucket.config["bucket"], folder))
    return ""


def _file(folder: str, file: str) -> str:
    return bucket.flask.send_from_directory(os.path.join(bucket.config["bucket"], folder), file)


def _files(folder: str) -> str:
    result: typing.Dict[str, typing.Dict[str, int]] = {}
    for file in os.scandir(os.path.join(bucket.config["bucket"], folder)):
        result[file.name] = dict(zip(("mode", "ino", "dev", "nlink", "uid", "gid", "size", "atime", "mtime", "ctime"), file.stat()))
    return bucket.flask.json.dumps(result)


def _put_file(folder: str, file: str) -> str:
    path: str = os.path.join(bucket.config["bucket"], folder)
    os.makedirs(path, exist_ok=True)
    path = os.path.join(path, bucket.werkzeug.utils.secure_filename(file))
    with open(path, "wb") as file:
        file.write(bucket.flask.request.data)
    return ""
