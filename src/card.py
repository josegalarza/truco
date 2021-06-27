NUMBERS = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
SUITS = ["espada", "basto", "oro", "copa"]


class Card:

    def __init__(self, num: int, suit: str):
        if num not in NUMBERS or suit not in SUITS:
            raise ValueError("Invalid card")
        self.num = num
        self.suit = suit

    def __str__(self):
        return f"{self.num}{self.suit[0]}"

    def get_envido(self) -> int:
        """Retorna puntos de envido de la carta."""
        return self.num if self.num < 10 else 0

    def get_truco(self) -> int:
        """Retorna el ranking en truco de la carta en orden descendente (1 más alta)."""
        if self.suit == "espada" and self.num == 1:
            return 1
        elif self.suit == "basto" and self.num == 1:
            return 2
        elif self.suit == "espada" and self.num == 7:
            return 3
        elif self.suit == "oro" and self.num == 7:
            return 4
        elif self.num == 3:
            return 5
        elif self.num == 2:
            return 6
        elif self.num == 1:
            return 7
        elif self.num == 12:
            return 8
        elif self.num == 11:
            return 9
        elif self.num == 10:
            return 10
        elif self.num == 7:
            return 11
        elif self.num == 6:
            return 12
        elif self.num == 5:
            return 13
        elif self.num == 4:
            return 14

    def id(self):
        return str(self)
