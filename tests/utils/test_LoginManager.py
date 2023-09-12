import sys
import typing

from gungnir.utils.LoginManager import LoginManager


class TestLoginManager:
    def setup_method(self: typing.Self, method) -> None:
        if method.__name__ == "test_shadow_loader":
            self.platform: str = sys.platform
            sys.platform = "dummy"

    def teardown_method(self: typing.Self, method) -> None:
        if method.__name__ == "test_shadow_loader":
            sys.platform = self.platform

    def test_shadow_loader(self: typing.Self) -> None:
        login_manager: LoginManager = LoginManager()
        login_manager._shadow_dummy = self._shadow_dummy
        login_manager.shadow_loader({"Authorization": "YWRtaW46YWRtaW4="})

    def _shadow_dummy(self: typing.Self, username: str, password: str) -> None:
        assert username == "admin" and password == "admin"
