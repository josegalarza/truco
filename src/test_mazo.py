from .mazo import Mazo


def test_init():
    m = Mazo()
    assert m is not None
    assert len(m.cartas) == 40
    assert m.cartas[0].get_id() == "1e"

def test_mezclar():
    m = Mazo()
    m.mezclar()
    assert m.cartas[0].get_id() != "1e"

def test_pop():
    m = Mazo()
    m.pop_carta()
    assert len(m.cartas) == 39

def test_repartir():
    m = Mazo()
    j1, j2 = m.repartir_cartas(jugadores=2)
    assert len(j1) == 3
    assert len(j2) == 3
