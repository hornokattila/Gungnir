import abc
from concurrent.futures.thread import ThreadPoolExecutor


class ThreadPool(abc.ABC):
    executor: ThreadPoolExecutor = ThreadPoolExecutor(1)

    def __init__(self, submit_folder: str) -> None:
        self.submit_folder: str = submit_folder
