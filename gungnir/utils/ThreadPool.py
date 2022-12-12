import os
from concurrent.futures.thread import ThreadPoolExecutor

from gungnir.utils.Environment import Environment

executor: ThreadPoolExecutor = ThreadPoolExecutor()


class ThreadPool:
    @staticmethod
    def submit(file: str, upload: str, logger: str) -> None:
        executor.submit(os.system, "{0} {1} {2} > {3}".format(Environment.RUNNER.decode(), file, upload, logger))
