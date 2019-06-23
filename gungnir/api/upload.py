from utils.Blueprint import Blueprint


class Upload(Blueprint):
    def init(self) -> None:
        pass


upload: Upload = Upload("upload", __name__)


@upload.route("/upload")
def _upload() -> str:
    return ""
