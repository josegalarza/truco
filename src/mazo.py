import random

from .carta import Carta


class Mazo:
    def __init__(self) -> None:
        self._init_cartas()

    def _init_cartas(self) -> None:
        self.cartas = [
            Carta(numero, palo)
            for palo in ("espada", "basto", "oro", "copa")
            for numero in (1, 2, 3, 4, 5, 6, 7, 10, 11, 12)
        ]

    def mezclar(self) -> None:
        """Shuffles the cards in the deck"""
        self._init_cartas()
        random.shuffle(self.cartas)
        random.shuffle(self.cartas)
        random.shuffle(self.cartas)

    def pop_carta(self) -> Carta:
        """Returns a card from the deck, None if deck is empty"""
        return self.cartas.pop(0) if self.cartas else None

    def repartir_cartas(self, jugadores: int) -> tuple:
        """Returns a jugadores-sized tuple of list of 3 Carta's."""
        result = tuple([] for i in range(jugadores))
        for j in range(jugadores):
            for c in range(3):
                result[j].append(self.pop_carta())
        return result

    # def get_all_deals(self):
    #     """Returns a list of all possible deals of 3 cards"""
    #     return [(c2, c2, c3)
    #             for c1 in self.cartas
    #             for c2 in self.cartas
    #             for c3 in self.cartas
    #             if len(set([c1, c2, c3])) == 3]
