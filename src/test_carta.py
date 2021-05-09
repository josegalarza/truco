import pytest

from .carta import Carta


def test_init():
    assert Carta(1, "espadas") is not None

def test_get_truco():
    assert Carta(1, "espadas").get_truco() == 1
    assert Carta(1, "basto").get_truco() == 2
    assert Carta(7, "espadas").get_truco() == 3
    assert Carta(7, "oro").get_truco() == 4
    assert Carta(3, "espadas").get_truco() == 5
    assert Carta(3, "basto").get_truco() == 5
    assert Carta(3, "oro").get_truco() == 5
    assert Carta(3, "copas").get_truco() == 5
    assert Carta(2, "espadas").get_truco() == 6
    assert Carta(2, "basto").get_truco() == 6
    assert Carta(2, "oro").get_truco() == 6
    assert Carta(2, "copas").get_truco() == 6
    assert Carta(1, "oro").get_truco() == 7
    assert Carta(1, "copas").get_truco() == 7
    assert Carta(12, "espadas").get_truco() == 8
    assert Carta(12, "basto").get_truco() == 8
    assert Carta(12, "oro").get_truco() == 8
    assert Carta(12, "copas").get_truco() == 8
    assert Carta(11, "espadas").get_truco() == 9
    assert Carta(11, "basto").get_truco() == 9
    assert Carta(11, "oro").get_truco() == 9
    assert Carta(11, "copas").get_truco() == 9
    assert Carta(10, "espadas").get_truco() == 10
    assert Carta(10, "basto").get_truco() == 10
    assert Carta(10, "oro").get_truco() == 10
    assert Carta(10, "copas").get_truco() == 10
    assert Carta(7, "basto").get_truco() == 11
    assert Carta(7, "copas").get_truco() == 11
    assert Carta(6, "espadas").get_truco() == 12
    assert Carta(6, "basto").get_truco() == 12
    assert Carta(6, "oro").get_truco() == 12
    assert Carta(6, "copas").get_truco() == 12
    assert Carta(5, "espadas").get_truco() == 13
    assert Carta(5, "basto").get_truco() == 13
    assert Carta(5, "oro").get_truco() == 13
    assert Carta(5, "copas").get_truco() == 13
    assert Carta(4, "espadas").get_truco() == 14
    assert Carta(4, "basto").get_truco() == 14
    assert Carta(4, "oro").get_truco() == 14
    assert Carta(4, "copas").get_truco() == 14

def test_get_envido():
    assert Carta(7, "oro").get_envido() == 7

def test_get_envido_2():
    assert Carta(11, "copas").get_envido() == 0

def test_carta_invalida():
    with pytest.raises(ValueError):
        assert Carta(9, "espadas")

def test_get_id():
    assert Carta(1, "espadas").get_id() == "1e"
