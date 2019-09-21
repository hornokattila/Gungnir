import os
import typing
import uuid

from utils.ThreadPool import ThreadPool


class Executor(ThreadPool):
    def __init__(self, logger_folder: str, submit_folder: str, upload_folder: str) -> None:
        super().__init__(submit_folder)
        self.logger_folder: str = logger_folder
        self.upload_folder: str = upload_folder

    def submit(self, json: typing.Dict[str, str]) -> str:
        try:
            self.validate(json)
            os.makedirs(self.submit_folder)
            name: str = uuid.uuid4().get_hex()
            path: str = os.path.join(self.submit_folder, "{0}.bat".format(name))
            with open(path, "x") as file:
                file.write(json["script"])
            self.executor.submit(os.system, "{0} {1} > {2}".format(path, self.upload_folder, os.path.join(self.logger_folder, "{0}.log".format(name))))
            self.executor.submit(os.remove, path)
            self.executor.submit(os.removedirs, self.submit_folder)
            return name
        except OSError:
            pass
        return ""

    def validate(self, json: typing.Dict[str, str]) -> None:
        if "script" not in json:
            raise ProcessLookupError()
