NUMBERS = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
SUITS = ["espada", "basto", "oro", "copa"]


class Card:

    def __init__(self, number: int, suit: str):
        if number not in NUMBERS or suit not in SUITS:
            raise ValueError("Invalid card")
        else:
            self.number = number
            self.suit = suit

    def __str__(self):
        return f"{self.number}{self.suit[0]}"

    def id(self):
        return str(self)

    def get_truco(self) -> int:
        """Retorna el ranking en truco de la carta en orden descendente (1 más alta)."""
        if self.suit == "espada" and self.number == 1:
            return 1
        elif self.suit == "basto" and self.number == 1:
            return 2
        elif self.suit == "espada" and self.number == 7:
            return 3
        elif self.suit == "oro" and self.number == 7:
            return 4
        elif self.number == 3:
            return 5
        elif self.number == 2:
            return 6
        elif self.number == 1:
            return 7
        elif self.number == 12:
            return 8
        elif self.number == 11:
            return 9
        elif self.number == 10:
            return 10
        elif self.number == 7:
            return 11
        elif self.number == 6:
            return 12
        elif self.number == 5:
            return 13
        elif self.number == 4:
            return 14

    def get_envido(self) -> int:
        """Retorna puntos de envido de la carta."""
        return self.number if self.number < 10 else 0
