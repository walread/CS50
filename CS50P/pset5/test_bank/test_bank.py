from bank import value


def test_hello():
    assert value("hello, mark") == 0


def test_h():
    assert value("hey, mark") == 20


def test_other():
    assert value("what's up, mark") == 100
