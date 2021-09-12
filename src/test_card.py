import pytest

from src.card import Card


def test_init():
    assert Card(1, "espada") is not None


def test_get_truco():
    assert Card(1, "espada").get_truco() == 1
    assert Card(1, "basto").get_truco() == 2
    assert Card(7, "espada").get_truco() == 3
    assert Card(7, "oro").get_truco() == 4
    assert Card(3, "espada").get_truco() == 5
    assert Card(3, "basto").get_truco() == 5
    assert Card(3, "oro").get_truco() == 5
    assert Card(3, "copa").get_truco() == 5
    assert Card(2, "espada").get_truco() == 6
    assert Card(2, "basto").get_truco() == 6
    assert Card(2, "oro").get_truco() == 6
    assert Card(2, "copa").get_truco() == 6
    assert Card(1, "oro").get_truco() == 7
    assert Card(1, "copa").get_truco() == 7
    assert Card(12, "espada").get_truco() == 8
    assert Card(12, "basto").get_truco() == 8
    assert Card(12, "oro").get_truco() == 8
    assert Card(12, "copa").get_truco() == 8
    assert Card(11, "espada").get_truco() == 9
    assert Card(11, "basto").get_truco() == 9
    assert Card(11, "oro").get_truco() == 9
    assert Card(11, "copa").get_truco() == 9
    assert Card(10, "espada").get_truco() == 10
    assert Card(10, "basto").get_truco() == 10
    assert Card(10, "oro").get_truco() == 10
    assert Card(10, "copa").get_truco() == 10
    assert Card(7, "basto").get_truco() == 11
    assert Card(7, "copa").get_truco() == 11
    assert Card(6, "espada").get_truco() == 12
    assert Card(6, "basto").get_truco() == 12
    assert Card(6, "oro").get_truco() == 12
    assert Card(6, "copa").get_truco() == 12
    assert Card(5, "espada").get_truco() == 13
    assert Card(5, "basto").get_truco() == 13
    assert Card(5, "oro").get_truco() == 13
    assert Card(5, "copa").get_truco() == 13
    assert Card(4, "espada").get_truco() == 14
    assert Card(4, "basto").get_truco() == 14
    assert Card(4, "oro").get_truco() == 14
    assert Card(4, "copa").get_truco() == 14


def test_get_envido():
    assert Card(7, "oro").get_envido() == 7


def test_get_envido_2():
    assert Card(11, "copa").get_envido() == 0


def test_invalid():
    with pytest.raises(ValueError):
        assert Card(9, "espada")


def test_id():
    assert Card(1, "espada").id() == "1e"
