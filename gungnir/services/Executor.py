from concurrent.futures.thread import ThreadPoolExecutor


class Executor(ThreadPoolExecutor):
    def __init__(self) -> None:
        super().__init__(1)
