import pytest

from carta import Carta


def test_init():
    assert Carta(1, "espadas") is not None

def test_get_truco():
    assert Carta(1, "espadas").get_truco() == 1

def test_get_truco_2():
    assert Carta(1, "basto").get_truco() == 2

def test_get_envido():
    assert Carta(7, "oro").get_envido() == 7

def test_get_envido_2():
    assert Carta(11, "copas").get_envido() == 0

def test_carta_invalida():
    with pytest.raises(ValueError):
        assert Carta(9, "espadas")

def test_get_id():
    assert Carta(1, "espadas").get_id() == "1e"
