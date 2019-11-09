import abc
import typing
from concurrent.futures.thread import ThreadPoolExecutor


class ThreadPool(abc.ABC):
    executor: ThreadPoolExecutor = ThreadPoolExecutor(1)

    def __init__(self, submit_folder: str) -> None:
        self.submit_folder: str = submit_folder

    @abc.abstractmethod
    def submit(self, json: typing.Dict[str, str]) -> typing.List[str]:
        pass

    @abc.abstractmethod
    def validate(self, json: typing.Dict[str, str]) -> None:
        pass
