from src.deck import Deck


class Dealer:

    def __init__(self):
        pass

    def deal(self, n: int):
        """Shuffles the deck and deals a hand of 3 cards to N players. Returns a N-sized tuple of 3 Cards."""
        d = Deck()
        d.shuffle()
        deal = tuple([] for _ in range(n))
        for _ in range(3):
            for i in range(n):
                card = d.pop()
                deal[i].append(card)
        return deal
