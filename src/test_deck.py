from .deck import Deck


def test_init():
    d = Deck()
    assert d is not None
    assert len(d._cards) == 40
    assert str(d._cards[0]) == "1e"


def test_shuffle():
    d = Deck()
    before = d._cards[:]
    d.shuffle()
    after = d._cards
    for c1, c2 in zip(before, after):
        if c1.id() != c2.id():
            assert True  # After shuffle, at least 1 card is on a different position.
            return
    assert False


def test_pop():
    d = Deck()
    before = len(d._cards)
    d.pop()
    assert len(d._cards) == before - 1
