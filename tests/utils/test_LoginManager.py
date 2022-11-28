import sys

import pytest

from gungnir.utils.LoginManager import LoginManager


class TestLoginManager:
    loginManager: LoginManager = LoginManager()

    def test_shadow_loader_negative(self) -> None:
        with pytest.raises(PermissionError):
            self.loginManager.shadow_loader({})

    def test_shadow_loader_positive(self) -> None:
        sys.platform = "win32"
        self.loginManager.shadow_loader({"Authorization": "Basic YTph"})
