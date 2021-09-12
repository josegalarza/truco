from .dealer import Dealer
<<<<<<< HEAD
from .player import Player


def test_init():
    player1 = Player("Jose")
    player2 = Player("Fran")
    dealer = Dealer(players=[player1, player2])
    assert dealer.players == [player1, player2]
    assert dealer.score == {player1: 0 , player2: 0}
=======


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
>>>>>>> main
