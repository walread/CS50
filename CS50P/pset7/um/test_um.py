from um import count

def test_inwords():
    assert count("yummy") == None

def test_space():
    assert count("um") == 1


def test_case():
    assert count("Um, thanks for the album.") == 1
