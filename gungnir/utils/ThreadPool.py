import abc
import typing
from concurrent.futures.thread import ThreadPoolExecutor


class ThreadPool(abc.ABC):
    executor: ThreadPoolExecutor = ThreadPoolExecutor(1)

    def validate(self, json: typing.Dict[str, str], keys: typing.List[str]) -> None:
        for key in keys:
            if key not in json:
                raise ProcessLookupError()
