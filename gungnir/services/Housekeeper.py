import os
import typing
from concurrent.futures.thread import ThreadPoolExecutor


class Housekeeper:
    def __init__(self, executor: ThreadPoolExecutor, submit_folder: str, upload_folder: str) -> None:
        self.executor: ThreadPoolExecutor = executor
        self.submit_folder: str = submit_folder
        self.upload_folder: str = upload_folder

    def polish(self, json: typing.Dict[str, str]) -> typing.List[str]:
        uploads: typing.List[str] = []
        try:
            self.validate(json)
            for file in os.scandir(self.upload_folder):
                if file.stat().st_size.__gt__(json["max_size"]):
                    self.executor.submit(os.remove, os.path.abspath(os.path.join(self.upload_folder, file.name)))
                    uploads.append(file.name)
        except OSError:
            pass
        return uploads

    def validate(self, json: typing.Dict[str, str]) -> None:
        if "max_size" not in json:
            raise ProcessLookupError()
