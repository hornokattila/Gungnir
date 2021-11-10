import os
import typing
from concurrent.futures.thread import ThreadPoolExecutor

from gungnir.utils.Environment import Environment

executor: ThreadPoolExecutor = ThreadPoolExecutor(1)


class ThreadPool:
    @staticmethod
    def submit(file: str, upload: str, logger: str) -> None:
        executor.submit(os.system, "{0} {1} {2} > {3}".format(Environment.RUNNER.decode(), file, upload, logger))

    @staticmethod
    def verify(json: typing.Dict[str, str], keys: typing.List[str]) -> None:
        if set(json.keys()) != set(keys):
            raise ProcessLookupError()
