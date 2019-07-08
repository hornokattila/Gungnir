from concurrent.futures.thread import ThreadPoolExecutor


class Executor(ThreadPoolExecutor):
    def __init__(self) -> None:
        super().__init__(1)

    def __new__(cls) -> "Executor":
        if not executor:
            return super().__new__(cls)
        return executor


executor: Executor = Executor()
