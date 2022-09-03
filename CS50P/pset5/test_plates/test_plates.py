from plates import is_valid


def test_start():
    assert is_valid("11AAAA") == False

def test_length():
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False

def test_numbers():
    assert is_valid("AA00AA") == False
    assert is_valid("AA022") == False

def test_punct():
    assert is_valid("A!A. A") == False