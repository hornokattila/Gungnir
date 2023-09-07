import os
import shutil
import tempfile
import time
import typing

from gungnir.utils.ThreadPool import ThreadPool


class TestThreadPool:
    def setup_method(self: typing.Self, method) -> None:
        if method.__name__ == "test_submit":
            self.file: tempfile.NamedTemporaryFile = tempfile.NamedTemporaryFile(delete=False)
            self.file.write(b"echo ACK")
            self.file.close()
            self.logger: tempfile.NamedTemporaryFile = tempfile.NamedTemporaryFile()
            self.upload: str = tempfile.mkdtemp()

    def teardown_method(self: typing.Self, method) -> None:
        if method.__name__ == "test_submit":
            os.unlink(self.file.name)
            self.logger.close()
            shutil.rmtree(self.upload)

    def test_submit(self: typing.Self) -> None:
        ThreadPool.submit(self.file.name, self.upload, self.logger.name)
        time.sleep(.2)
        assert self.logger.read() == b"ACK\n"
