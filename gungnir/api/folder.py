import os
import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Folder(Blueprint):
    def detail(self) -> typing.Dict[str, typing.Dict[str, typing.Union[str, typing.List[str]]]]:
        return {
            "_delete_file": {"rule": "/folders/<path>/<file>", "methods": ["DELETE"]},
            "_file": {"rule": "/folders/<path>/<file>", "methods": ["GET"]},
            "_files": {"rule": "/folders/<path>", "methods": ["GET"]},
            "_post_file": {"rule": "/folders/<path>", "methods": ["POST"]}
        }

    def enable(self) -> None:
        for path in self.folder.values():
            os.makedirs(path, exist_ok=True)


folder: Folder = Folder(LoginManager().shadow_loader)


@folder.route(**folder.detail()["_delete_file"])
def _delete_file(path: str, file: str) -> str:
    os.remove(os.path.join(folder.folder[path], file))
    return ""


@folder.route(**folder.detail()["_file"])
def _file(path: str, file: str) -> str:
    return folder.flask.send_from_directory(folder.folder[path], file)


@folder.route(**folder.detail()["_files"])
def _files(path: str) -> str:
    result: typing.Dict[str, typing.Dict[str, int]] = {}
    for file in os.scandir(folder.folder[path]):
        result[file.name] = dict(zip(("mode", "ino", "dev", "nlink", "uid", "gid", "size", "atime", "mtime", "ctime"), file.stat()))
    return folder.flask.json.dumps(result)


@folder.route(**folder.detail()["_post_file"])
def _post_file(path: str) -> str:
    for file in folder.flask.request.files:
        name: str = folder.werkzeug.utils.secure_filename(file)
        folder.flask.request.files[name].save(os.path.join(folder.folder[path], name))
    return ""
