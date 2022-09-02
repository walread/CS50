from twttr import shorten

def test_shorten():
    vowel = "AEIOUaeiou"
    for c in vowel:
        assert c not in shorten("cat")
