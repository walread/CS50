from twttr import shorten

def test_lower():
    vowel = "AEIOUaeiou"
    for c in vowel:
        assert c not in shorten("cat")

def test_upper():
    vowel = "AEIOUaeiou"
    for c in vowel:
        assert c not in shorten("CAT")
