from src.dealer import Dealer


def test_init():
    d = Dealer()
    assert d is not None


def test_deal():
    d = Dealer()
    n = 2
    x = d.deal(n)
    assert len(x) == n
    for i in range(n):
        assert len(x[i]) == 3
