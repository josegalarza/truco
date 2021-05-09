class Player:
    def __init__(self, name: str):
        self.name = f"{name}"
        self.cards = []

    def __str__(self):
        return self.name
