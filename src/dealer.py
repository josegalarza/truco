# Represents the dealer and runner of the game.
from itertools import cycle

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

    def play(self, autoplay=False):
        os.system("clear")
        p1 = self.players[0]
        p2 = self.players[1]
        for mano, pie in cycle([(p1, p2), (p2, p1)]):
            if self._game_over():
                break
            else:
                self.play_round(mano, pie, autoplay)
                print(f"Score: {p1} {self.score[p1]} - {p2} {self.score[p2]}\n")
        print("Game over!")

    def _game_over(self):
        for key, value in self.score.items():
            if value >= 30:
                return True
        return False
        # return self.score[0] >= 30 or self.score[1] >= 30

    def play_round(self, mano, pie, autoplay=False):
        # Shuffle cards and deal
        deck = self.deck
        deck.mezclar()
        mano_cards, pie_cards = deck.repartir_cartas(jugadores=2)
        mano.cards = mano_cards
        pie.cards = pie_cards
        # play envido
        self._play_envido(mano, pie)
        if self._game_over():
            return
        # play truco
        self._play_truco(mano, pie, autoplay)

    def _play_envido(self, mano, pie, autoplay=False):
        print("Envido!")
        print(f"{mano}: {mano.get_envido()}")
        print(f"{pie}: {pie.get_envido()}")
        winner = mano if mano.get_envido() >= pie.get_envido() else pie
        print(f"{winner}, won! (+2 points)\n")
        self.score[winner] += 2

    def _play_truco(self, mano, pie, autoplay=False):
        score = {mano: 0, pie: 0}
        print("Truco!")
        winner = None

        # first
        # play cards
        print("1)")
        c1 = mano.play_card(autoplay=autoplay)
        print(f"{mano.name}: {c1}")
        c2 = pie.play_card(autoplay=autoplay)
        print(f"{pie.name}: {c2}")
        # count score
        if c1.get_truco() < c2.get_truco():
            score[mano] += 1  # mano won
            winner = mano
        elif c1.get_truco() == c2.get_truco():
            score[mano] += 1  # mano tied
            score[pie] += 1  # mano tied
            winner = mano
        elif c1.get_truco() > c2.get_truco():
            winner = pie
            score[pie] += 1  # pie won

        # second
        print("2)")
        # play cards
        if winner == mano:  # mano won or tied, keeps playing
            c1 = mano.play_card(autoplay=autoplay)
            print(f"{mano.name}: {c1}")
            c2 = pie.play_card(autoplay=autoplay)
            print(f"{pie.name}: {c2}")
        else:
            c2 = pie.play_card(autoplay=autoplay)
            print(f"{pie.name}: {c2}")
            c1 = mano.play_card(autoplay=autoplay)
            print(f"{mano.name}: {c1}")
        # count score
        if c1.get_truco() < c2.get_truco():
            score[mano] += 1  # mano won
            winner = mano
        elif c1.get_truco() == c2.get_truco():
            score[mano] += 1  # mano tied
            score[pie] += 1  # mano tied
            winner = mano
        elif c1.get_truco() > c2.get_truco():
            score[pie] += 1  # pie won
            winner = pie
        # over?
        if score[mano] == 2:
            self.score[mano] += 2
            print(f"{mano.name} won! (+2 points)\n")
            return
        elif score[pie] == 2:
            self.score[pie] += 2
            print(f"{pie.name} won! (+2 points)\n")
            return

        # Third
        print("3)")
        # play cards
        if winner == mano:  # mano won or tied, keeps playing
            c1 = mano.play_card(autoplay=autoplay)
            print(f"{mano.name}: {c1}")
            c2 = pie.play_card(autoplay=autoplay)
            print(f"{pie.name}: {c2}")
        else:
            c2 = pie.play_card(autoplay=autoplay)
            print(f"{pie.name}: {c2}")
            c1 = mano.play_card(autoplay=autoplay)
            print(f"{mano.name}: {c1}")
        # count score
        if c1.get_truco() < c2.get_truco():
            score[mano] += 1  # mano won
            winner = mano
        elif c1.get_truco() == c2.get_truco():
            score[mano] += 1  # mano tied
            score[pie] += 1  # mano tied
            winner = mano
        elif c1.get_truco() > c2.get_truco():
            score[pie] += 1  # pie won
            winner = pie
        # over?
        if score[mano] == 3:
            self.score[mano] += 2
            print(f"{mano.name} won! (+2 points)\n")
            return
        elif score[pie] == 3:
            self.score[pie] += 2
            print(f"{pie.name} won! (+2 points)\n")
            return
        elif score[mano] == 2:
            self.score[mano] += 2
            print(f"{mano.name} won! (+2 points)\n")
            return
        elif score[pie] == 2:
            self.score[pie] += 2
            print(f"{pie.name} won! (+2 points)\n")
            return
