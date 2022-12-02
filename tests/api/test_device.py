from gungnir.api.device import device


class TestDevice:
    def test_health(self) -> None:
        result: bool = False
        for detail in device.detail():
            if detail["rule"] == "/health":
                result |= detail["view_func"]() == ""
        assert result
