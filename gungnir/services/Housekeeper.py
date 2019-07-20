import typing
from concurrent.futures.thread import ThreadPoolExecutor


class Housekeeper:
    def __init__(self, executor: ThreadPoolExecutor, submit_folder: str, upload_folder: str) -> None:
        self.executor: ThreadPoolExecutor = executor
        self.submit_folder: str = submit_folder
        self.upload_folder: str = upload_folder

    def attach(self, json: typing.Dict[str, str]) -> str:
        return ""
