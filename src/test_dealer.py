from .dealer import Dealer
from .player import Player


def test_init():
    player1 = Player("Jose")
    player2 = Player("Fran")
    dealer = Dealer(players=[player1, player2])
    assert dealer.players == [player1, player2]
    assert dealer.score == {player1: 0 , player2: 0}
