import pytest

from .carta import Carta


def test_init():
    assert Carta(1, "espada") is not None

def test_get_truco():
    assert Carta(1, "espada").get_truco() == 1
    assert Carta(1, "basto").get_truco() == 2
    assert Carta(7, "espada").get_truco() == 3
    assert Carta(7, "oro").get_truco() == 4
    assert Carta(3, "espada").get_truco() == 5
    assert Carta(3, "basto").get_truco() == 5
    assert Carta(3, "oro").get_truco() == 5
    assert Carta(3, "copa").get_truco() == 5
    assert Carta(2, "espada").get_truco() == 6
    assert Carta(2, "basto").get_truco() == 6
    assert Carta(2, "oro").get_truco() == 6
    assert Carta(2, "copa").get_truco() == 6
    assert Carta(1, "oro").get_truco() == 7
    assert Carta(1, "copa").get_truco() == 7
    assert Carta(12, "espada").get_truco() == 8
    assert Carta(12, "basto").get_truco() == 8
    assert Carta(12, "oro").get_truco() == 8
    assert Carta(12, "copa").get_truco() == 8
    assert Carta(11, "espada").get_truco() == 9
    assert Carta(11, "basto").get_truco() == 9
    assert Carta(11, "oro").get_truco() == 9
    assert Carta(11, "copa").get_truco() == 9
    assert Carta(10, "espada").get_truco() == 10
    assert Carta(10, "basto").get_truco() == 10
    assert Carta(10, "oro").get_truco() == 10
    assert Carta(10, "copa").get_truco() == 10
    assert Carta(7, "basto").get_truco() == 11
    assert Carta(7, "copa").get_truco() == 11
    assert Carta(6, "espada").get_truco() == 12
    assert Carta(6, "basto").get_truco() == 12
    assert Carta(6, "oro").get_truco() == 12
    assert Carta(6, "copa").get_truco() == 12
    assert Carta(5, "espada").get_truco() == 13
    assert Carta(5, "basto").get_truco() == 13
    assert Carta(5, "oro").get_truco() == 13
    assert Carta(5, "copa").get_truco() == 13
    assert Carta(4, "espada").get_truco() == 14
    assert Carta(4, "basto").get_truco() == 14
    assert Carta(4, "oro").get_truco() == 14
    assert Carta(4, "copa").get_truco() == 14

def test_get_envido():
    assert Carta(7, "oro").get_envido() == 7

def test_get_envido_2():
    assert Carta(11, "copa").get_envido() == 0

def test_carta_invalida():
    with pytest.raises(ValueError):
        assert Carta(9, "espada")

def test_get_id():
    assert Carta(1, "espada").get_id() == "1e"
