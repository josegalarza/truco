# Represents the dealer and runner of the game.

from .mazo import Mazo as Deck

class Dealer:

    def __init__(self, players):
        if len(players) != 2:
            raise ValueError("Requires 2 players.")
        self.deck = Deck()
        self.players = players
        self.score = {
            self.players[0]: 0,
            self.players[1]: 0,
        }
        pass

    def play(self):
        p1 = self.players[0]
        p2 = self.players[1]
        for mano, pie in cycle([(p1, p2), (p2, p1)]):
            while not self._game_over():
                self.play_round(mano, pie)
        print("Game over!")

    def _game_over(self):
        return self.score[0] >= 30 or self.score[1] >= 30

    def play_round(self, mano, pie):
        deck = self.deck()
        deck.mezclar()
        mano_cards, pie_cards = deck.repartir_cartas(jugadores=2)
        mano.cards = mano_cards
        pie.cards = pie_cards

        winner = mano if mano.cards[0].get_truco() >= pie.cards[0].get_truco() else pie
        self.score[winner] += 1
        print(f"Round winner player: {winner}")

