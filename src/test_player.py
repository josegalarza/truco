from src.player import Player


def test_init():
    player = Player(name="Jose")
    assert player is not None
    assert player.name == "Jose"
    assert player.cards == []


def test_print():
    player = Player(name="Jose")
    assert str(player) == "Jose"
