class Carta:
    def __init__(self, numero: int, palo: str):
        if (
            numero in (1, 2, 3, 4, 5, 6, 7, 10, 11, 12)
            and palo in("espada", "basto", "oro", "copa")
        ):
            self.numero = numero
            self.palo = palo
        else:
            raise ValueError("Carta invalida")

    def __str__(self):
        return f"{self.numero}{self.palo[0]}"

    def get_id(self):
        return str(self)

    def get_truco(self) -> int:
        """Retorna el ranking en truco de la carta en orden descendente (1 más alta)."""
        if self.palo == "espada" and self.numero == 1:
            return 1
        elif self.palo == "basto" and self.numero == 1:
            return 2
        elif self.palo == "espada" and self.numero == 7:
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

    def get_envido(self) -> int:
        """Retorna puntos de envido de la carta."""
        return self.numero if self.numero < 10 else 0
