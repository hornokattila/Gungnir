import abc
from concurrent.futures.thread import ThreadPoolExecutor


class ThreadPool(abc.ABC):
    executor: ThreadPoolExecutor = ThreadPoolExecutor(1)
