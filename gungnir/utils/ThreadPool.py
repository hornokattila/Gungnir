import os
import typing
from concurrent.futures.thread import ThreadPoolExecutor

executor: ThreadPoolExecutor = ThreadPoolExecutor(1)


class ThreadPool:
    @staticmethod
    def submit(shebang: str, file: str, upload: str, logger: str) -> None:
        # TODO: FIXME!
        executor.submit(os.system, "{0} {1} {2} > {3}".format(shebang, file, upload, logger))
        executor.submit(os.remove, file)

    @staticmethod
    def verify(json: typing.Dict[str, str], keys: typing.List[str]) -> None:
        if set(json.keys()) != set(keys):
            raise ProcessLookupError()
