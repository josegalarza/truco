from random import choice


class Player:
    def __init__(self, name: str):
        self.name = f"{name}"
        self.cards = []

    def __str__(self):
        return self.name

    def get_card(self, auto=False):
        if auto:
            card = choice(self.cards)
        else:
            print("What card will you play?")
            for i in range(len(self.cards)):
                print(f"{i}. {self.cards[i]}")
            i = int(input())
            card = self.cards[i]
        self.cards.remove(card)
        return card
