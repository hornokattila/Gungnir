import typing
from concurrent.futures.thread import ThreadPoolExecutor

executor: ThreadPoolExecutor = ThreadPoolExecutor(1)


class ThreadPool:
    @staticmethod
    def submit(rule: typing.Callable[[str], typing.Union[int, None]], args: str) -> None:
        executor.submit(rule, args)

    @staticmethod
    def verify(json: typing.Dict[str, str], keys: typing.List[str]) -> None:
        if set(json.keys()) != set(keys):
            raise ProcessLookupError()

    @staticmethod
    def volume() -> int:
        return executor._work_queue.qsize()
