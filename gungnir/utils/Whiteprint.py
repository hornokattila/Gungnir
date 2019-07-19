from concurrent.futures.thread import ThreadPoolExecutor

from utils.Blueprint import Blueprint


class Whiteprint(Blueprint):
    def __init__(self, name: str, import_name: str) -> None:
        self.executor: ThreadPoolExecutor = ThreadPoolExecutor(1)
        super().__init__(name, import_name)

    def init(self) -> None:
        pass
