import typing
from concurrent.futures.thread import ThreadPoolExecutor


class ThreadPool:
    executor: ThreadPoolExecutor = ThreadPoolExecutor(1)

    @staticmethod
    def submit(function: typing.Callable[[str], typing.Union[int, None]], args: str):
        ThreadPool.executor.submit(function, args)

    @staticmethod
    def validate(json: typing.Dict[str, str], keys: typing.List[str]) -> None:
        for prop in keys:
            if prop not in json:
                raise ProcessLookupError()
