import fuel

def test_convert():
    assert fuel.convert("1/10") == 0.1


def test_gauge():
    assert fuel.gauge(0.5) == "50%"
