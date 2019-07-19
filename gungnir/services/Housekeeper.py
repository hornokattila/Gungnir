import typing
from concurrent.futures.thread import ThreadPoolExecutor


class Housekeeper:
    def __init__(self, executor: ThreadPoolExecutor, settings: typing.Dict[str, str], submit_folder: str, upload_folder: str) -> None:
        self.executor: ThreadPoolExecutor = executor
        self.settings: typing.Dict[str, str] = settings
        self.submit_folder: str = submit_folder
        self.upload_folder: str = upload_folder

    def attach(self) -> str:
        return ""
