from gungnir.api.device import Device


class TestDevice:
    device: Device = Device(lambda map: None)

    def test_health(self) -> None:
        result: bool = False
        for detail in self.device.detail():
            if detail["rule"] == "/health":
                result |= detail["view_func"]() == ""
        assert result
