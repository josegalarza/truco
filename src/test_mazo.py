from .mazo import Mazo


def test_init():
    m = Mazo()
    assert m is not None
    assert len(m.cartas) == 40
    assert m.cartas[0].get_id() == "1e"

def test_mezclar():
    m = Mazo()
    m.mezclar()
    m.mezclar()
    m.mezclar()
    assert m.cartas[0].get_id() != "1e"

def test_pop():
    m = Mazo()
    m.pop_carta()
    assert len(m.cartas) == 39
