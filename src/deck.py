import random

from .card import Card, NUMBERS, SUITS


class Deck:

    def __init__(self) -> None:
        self._cards = [
            Card(num, suit)
            for suit in SUITS  # 🗡 🌳 🥇 🏆
            for num in NUMBERS
        ]

    def shuffle(self) -> None:
        """Shuffles the cards in the deck."""
        random.shuffle(self._cards)

    def pop(self) -> Card:
        """Returns a card from the deck. Returns None if deck is empty."""
        return self._cards.pop(0) if self._cards else None
