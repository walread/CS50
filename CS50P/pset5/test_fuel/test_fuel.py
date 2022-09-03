import fuel
import pytest

def test_convert():
    assert fuel.convert("1/10") == 10
    with pytest.raises(TypeError):
        fuel.convert("s/s")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")


def test_gauge():
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(1) == "E"
