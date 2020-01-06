import typing
from concurrent.futures.thread import ThreadPoolExecutor

executor: ThreadPoolExecutor = ThreadPoolExecutor(1)


class ThreadPool:
    @staticmethod
    def submit(record: typing.Callable[[str], typing.Union[int, None]], args: str):
        executor.submit(record, args)

    @staticmethod
    def verify(json: typing.Dict[str, str], keys: typing.List[str]) -> None:
        if set(json.keys()) != set(keys):
            raise ProcessLookupError()
