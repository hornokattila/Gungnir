import abc
import typing
from concurrent.futures.thread import ThreadPoolExecutor


class ThreadPool(abc.ABC):
    executor: ThreadPoolExecutor = ThreadPoolExecutor(1)

    def validate(self, json: typing.Dict[str, str], keys: typing.List[str]) -> None:
        for prop in keys:
            if prop not in json:
                raise ProcessLookupError()
