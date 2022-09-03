import fuel

def test_convert():
    assert fuel.convert("1/10") == 10


def test_gauge():
    assert fuel.gauge(50) == "50%"
