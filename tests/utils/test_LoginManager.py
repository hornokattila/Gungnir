import pytest

from gungnir.utils.LoginManager import LoginManager


class TestLoginManager:
    loginManager: LoginManager = LoginManager()

    def test_shadow_loader_negative(self) -> None:
        with pytest.raises(PermissionError):
            self.loginManager.shadow_loader({})

    def test_shadow_loader_positive(self) -> None:
        self.loginManager.shadow_loader({"Authorization": "Basic YTph"})
