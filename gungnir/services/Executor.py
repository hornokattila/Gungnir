import os
import typing
import uuid
from concurrent.futures.thread import ThreadPoolExecutor


class Executor:
    def __init__(self, executor: ThreadPoolExecutor, logger_folder: str, submit_folder: str, upload_folder: str) -> None:
        self.executor: ThreadPoolExecutor = executor
        self.logger_folder: str = logger_folder
        self.submit_folder: str = submit_folder
        self.upload_folder: str = upload_folder

    def submit(self, json: typing.Dict[str, str]) -> str:
        try:
            self.validate(json)
            os.makedirs(self.submit_folder)
            name: str = uuid.uuid4().get_hex()
            logger_path: str = os.path.join(self.logger_folder, "{0}.log".format(name))
            submit_path: str = os.path.join(self.submit_folder, "{0}.bat".format(name))
            with open(submit_path, "x") as file:
                file.write(json["script"])
            self.executor.submit(os.system, "{0} {1} > {2}".format(submit_path, self.upload_folder, logger_path))
            self.executor.submit(os.remove, submit_path)
            self.executor.submit(os.removedirs, self.submit_folder)
            return name
        except OSError:
            pass
        return ""

    def validate(self, json: typing.Dict[str, str]) -> None:
        if "script" not in json:
            raise ProcessLookupError()
