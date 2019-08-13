import os
import typing
from concurrent.futures.thread import ThreadPoolExecutor


class Housekeeper:
    def __init__(self, executor: ThreadPoolExecutor, submit_folder: str, upload_folder: str) -> None:
        self.executor: ThreadPoolExecutor = executor
        self.submit_folder: str = submit_folder
        self.upload_folder: str = upload_folder

    def attach(self, json: typing.Dict[str, str]) -> str:
        try:
            self.validate(json)
            for file in os.scandir(self.upload_folder):
                if file.stat().st_size.__gt__(json["max_size"]):
                    # TODO: Sample implementation.
                    pass
        except OSError:
            pass
        return ""

    def validate(self, json: typing.Dict[str, str]) -> None:
        if "max_size" not in json:
            raise ProcessLookupError()
