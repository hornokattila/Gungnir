import shutil
import tempfile

from gungnir.utils.ThreadPool import ThreadPool


class TestThreadPool:
    def test_submit(self) -> None:
        file: tempfile.NamedTemporaryFile = tempfile.NamedTemporaryFile()
        upload: str = tempfile.mkdtemp()
        logger: str = tempfile.mkdtemp()
        file.write(b"echo YOLO")
        file.seek(0)
        ThreadPool.submit(file.name, upload, logger)
        file.close()
        shutil.rmtree(upload)
        shutil.rmtree(logger)
