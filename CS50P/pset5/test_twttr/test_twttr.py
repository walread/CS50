from twttr import shorten

def test_shorten():
    assert shorten("1Apple!") == ("1ppl!")
