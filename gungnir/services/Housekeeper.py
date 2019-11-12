import os
import typing

from utils.ThreadPool import ThreadPool


class Housekeeper:
    def __init__(self, submit_folder: str, upload_folder: str) -> None:
        self.submit_folder: str = submit_folder
        self.upload_folder: str = upload_folder

    def submit(self, json: typing.Dict[str, str]) -> typing.List[str]:
        uploads: typing.List[str] = []
        try:
            ThreadPool.validate(json, ["max_size"])
            for file in os.scandir(self.upload_folder):
                if file.stat().st_size.__gt__(json["max_size"]):
                    name: str = file.name
                    ThreadPool.submit(os.remove, os.path.join(self.upload_folder, name))
                    uploads.append(name)
        except OSError:
            pass
        return uploads
