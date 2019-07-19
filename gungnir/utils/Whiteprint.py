from concurrent.futures.thread import ThreadPoolExecutor

from utils.Blueprint import Blueprint


class Whiteprint(Blueprint):
    executor: ThreadPoolExecutor = ThreadPoolExecutor(1)

    def init(self) -> None:
        pass
