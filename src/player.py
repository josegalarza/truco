import random


class Player:
    def __init__(self, name: str):
        self.name = f"{name}"
        self.cards = []

    def __str__(self):
        return self.name

    def get_envido(self):
        """Returns how many envido points the player has."""
        if not self.cards:
            raise RuntimeError("Missing cards")
        c1, c2, c3 = sorted(self.cards, key = lambda x: (-x.get_envido()))
        if c1.palo == c2.palo:
            return c1.get_envido() + c2.get_envido() + 20
        elif c1.palo == c3.palo:
            return c1.get_envido() + c3.get_envido() + 20
        elif c2.palo == c3.palo:
            return c2.get_envido() + c3.get_envido() + 20
        else:
            return c1.get_envido()

    def get_truco(self):
        """Returns a sorted list of card's truco rankins."""
        if not self.cards:
            raise RuntimeError("Missing cards")
        return sorted(self.cards, key = lambda x: (x.get_truco()))

    def play_card(self, random_choice=False):
        if random_choice:
            card = random.choice(self.cards)
        else:
            print(f"{self.name}, play a card!")
            for i in range(len(self.cards)):
                print(f"{i}) {self.cards[i]}")
            i = int(input("Enter choice number: "))
            card = self.cards[i]
        self.cards.remove(card)
        return card
