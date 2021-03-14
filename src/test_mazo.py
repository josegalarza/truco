from .mazo import Mazo


def test_init():
    m = Mazo()
    assert m is not None
    assert len(m.cartas) == 40
    assert m.cartas[0].get_id() == "1e"


def test_mezclar():
    m = Mazo()
    before = m.cartas[:]
    m.mezclar()
    after = m.cartas
    for c1, c2 in zip(before, after):
        if c1.get_id() != c2.get_id():
            assert True  # After mezclar, at least 1 carta is on a different position.
            return
    assert False


def test_pop():
    m = Mazo()
    before = len(m.cartas)
    m.pop_carta()
    assert len(m.cartas) == before - 1


def test_repartir():
    m = Mazo()
    j1, j2 = m.repartir_cartas(jugadores=2)
    assert len(j1) == 3
    assert len(j2) == 3
