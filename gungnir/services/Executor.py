import os
import typing
import uuid


class Executor:
    def __init__(self, logger_folder: str, submit_folder: str, upload_folder: str) -> None:
        self.logger_folder: str = logger_folder
        self.submit_folder: str = submit_folder
        self.upload_folder: str = upload_folder

    def submit(self, json: typing.Dict[str, str]) -> str:
        try:
            os.makedirs(self.submit_folder)
            name: str = uuid.uuid4().hex
            path: str = os.path.join(self.submit_folder, ".".join([name, "sh"]))
            with open(path, "x") as file:
                file.write(json["script"])
            return name
        except OSError:
            pass
        return ""
