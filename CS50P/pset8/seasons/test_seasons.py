from seasons import convert
from pytest import raises


def test_convert():
    assert convert("2021-10-06") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert("2020-10-06") == "One million, fifty-one thousand, two hundred minutes"
    with raises(SystemExit):
        convert("2021/10/06")
