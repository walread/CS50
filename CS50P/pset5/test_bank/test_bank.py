from bank import value


def test_hello():
    assert value("Hello, Mark") == 0


def test_h():
    assert value("Hey, Mark") == 20


def test_other():
    assert value("What's up, Mark") == 100
