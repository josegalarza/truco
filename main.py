#!/usr/bin/env python
# Truco Argentino
# Interesting read: https://github.com/IAARhub/TrucoAnalytics
import random


class Card:
    def __init__(self, palo, numero):
        self.palo = palo
        self.numero = numero
        
    def __str__(self):
        return f"{self.numero}{self.palo[0]}"

    def get_truco_ranking(self):
        if self.palo == "espadas" and self.numero == 1:
            return 1
        elif self.palo == "basto" and self.numero == 2:
            return 2
        elif self.palo == "espadas" and self.numero == 7:
            return 3
        elif self.palo == "oro" and self.numero == 7:
            return 4
        elif self.numero == 3:
            return 5
        elif self.numero == 2:
            return 6
        elif self.numero == 1:
            return 7
        elif self.numero == 12:
            return 8
        elif self.numero == 11:
            return 9
        elif self.numero == 10:
            return 10
        elif self.numero == 7:
            return 11
        elif self.numero == 6:
            return 12
        elif self.numero == 5:
            return 13
        elif self.numero == 4:
            return 14

    def get_envido_puntos(self):
        return self.numero if self.numero < 10 else 0


class Deck:
    __cards = [
        # espadas 🗡
        Card("espadas",  1),
        Card("espadas",  2),
        Card("espadas",  3),
        Card("espadas",  4),
        Card("espadas",  5),
        Card("espadas",  6),
        Card("espadas",  7),
        Card("espadas", 10),
        Card("espadas", 11),
        Card("espadas", 12),
        # basto 🌵
        Card("basto",  1),
        Card("basto",  2),
        Card("basto",  3),
        Card("basto",  4),
        Card("basto",  5),
        Card("basto",  6),
        Card("basto",  7),
        Card("basto", 10),
        Card("basto", 11),
        Card("basto", 12),
        # oro 🥇
        Card("oro",  1),
        Card("oro",  2),
        Card("oro",  3),
        Card("oro",  4),
        Card("oro",  5),
        Card("oro",  6),
        Card("oro",  7),
        Card("oro", 10),
        Card("oro", 11),
        Card("oro", 12),
        # copas 🏆
        Card("copas",  1),
        Card("copas",  2),
        Card("copas",  3),
        Card("copas",  4),
        Card("copas",  5),
        Card("copas",  6),
        Card("copas",  7),
        Card("copas", 10),
        Card("copas", 11),
        Card("copas", 12),
    ]
    # Shorter way
    # __cards = []
    # for palo in ["espadas", "basto", "oro", "copas"]:
    #     for numero in [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]:
    #         __cards.append(Card(palo, numero))


    def __init__(self):
        self.cards = self.__cards[:]

    def hit(self):
        """Returns a card from the deck, None if deck is empty"""
        return self.cards.pop(0) if self.cards else None

    def shuffle(self):
        """Shuffles the cards in the deck"""
        self.cards = self.__cards[:]
        random.shuffle(self.cards)


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.cards = []

    def __str__(self):
        return (f"Name: {self.name}, "
            + f"Score: {self.score}, "
            + f"Cards: {', '.join([f'{card}' for card in self.cards])}, "
            + f"Envido: {self.get_envido_puntos()}"
        )

    def get_envido_puntos(self):
        c0 = self.cards[0]
        c1 = self.cards[1]
        c2 = self.cards[2]        
        if c0.palo == c1.palo == c2.palo:
            # If flor: sum 2 highest
            sorted_cards = sorted(self.cards, key = lambda x: (-x.get_envido_puntos()))
            return sorted_cards[0].get_envido_puntos() + sorted_cards[1].get_envido_puntos() + 20
        elif c0.palo == c1.palo:
            return c0.get_envido_puntos() + c1.get_envido_puntos() + 20
        elif c0.palo == c2.palo:
            return c0.get_envido_puntos() + c2.get_envido_puntos() + 20
        elif c1.palo == c2.palo:
            return c1.get_envido_puntos() + c2.get_envido_puntos() + 20
        else:
            # If no envido: get highest
            sorted_cards = sorted(self.cards, key = lambda x: (-x.get_envido_puntos()))
            return sorted_cards[0].get_envido_puntos()


class Table:
    def __init__(self):
        self.deck = Deck()

    def deal(self, player1, player2):
        self.deck.shuffle()
        player1.cards.append(self.deck.hit())
        player2.cards.append(self.deck.hit())
        player1.cards.append(self.deck.hit())
        player2.cards.append(self.deck.hit())
        player1.cards.append(self.deck.hit())
        player2.cards.append(self.deck.hit())


def demo():
    print("Truco - @josegalarza 2020")

    jose = Player("Jose")
    fran = Player("Fran")

    mesa = Table()
    mesa.deal(jose, fran)

    print(jose)
    print(fran)


if __name__ == "__main__":
    demo()
