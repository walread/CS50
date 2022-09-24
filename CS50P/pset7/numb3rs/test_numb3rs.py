from numb3rs import validate


def test_valid():
    assert validate("255.255.255.255") == True
    assert validate("000.000.000.000") == True


def test_invalid():
    assert validate("0000.1.2.3") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
