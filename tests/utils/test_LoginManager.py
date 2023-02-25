import sys

from gungnir.utils.LoginManager import LoginManager


class TestLoginManager:
    def test_shadow_loader(self) -> None:
        sys.platform = "dummy"
        login_manager: LoginManager = LoginManager()
        login_manager._shadow_dummy = TestLoginManager._shadow_dummy
        login_manager.shadow_loader({"Authorization": "YWRtaW46YWRtaW4="})

    @staticmethod
    def _shadow_dummy(username: str, password: str) -> None:
        assert username == "admin" and password == "admin"
