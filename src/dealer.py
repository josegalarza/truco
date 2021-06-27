from .deck import Deck


class Dealer:

    def __init__(self):
        pass

    def deal(self, n: int):
        """Deal. Returns N hands of 3 cards each."""
        d = Deck()
        d.shuffle()
        deal = tuple([] for _ in range(n))
        for _ in range(3):
            for i in range(n):
                card = d.pop()
                deal[i].append(card)
        return deal
