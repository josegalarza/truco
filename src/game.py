from .dealer import Dealer


class Game:

    def __init__(self, players=[None, None]):
        self.players = players
        self.score = {self.players[0]: 0, self.players[1]: 0}
        self.dealer = Dealer()

    def is_over(self):
        return self.get_winner() is not None


    def get_winner(self):
        for player, score in self.score.items():
            if score >= 30:
                return player
        return None


    def play(self):
        mano = self.players[0]
        pie = self.players[1]

        while True:
            cards_mano, cards_pie = self.dealer.deal(n=2)
            mano.cards = cards_mano
            pie.cards = cards_pie

            # TODO: play round
            self.play_round(mano, pie)
            print(f"Score: {self.score[self.players[0]]}-{self.score[self.players[1]]}")

            if self.is_over():
                print(f"Winner: {self.get_winner()}")
                return
            else:
                mano, pie = pie, mano


    def play_round(self, player_1, player_2):
        result = [None, None, None]  # results of first, second y third

        # first
        mano = player_1
        pie = player_2
        card_mano = mano.get_card(auto=True)
        card_pie = pie.get_card(auto=True)
        print(f"Player {mano.name} plays {card_mano}, player {pie.name} plays {card_pie}.")

        if card_mano.get_truco() < card_pie.get_truco():
            result[0] = mano
        elif card_mano.get_truco() == card_pie.get_truco():
            result[0] = None
        else:
            result[0] = pie

        # second
        if result[0] == player_2:
            mano, pie = player_2, player_1  # P2 won, P2 plays next

        card_mano = mano.get_card(auto=True)
        card_pie = pie.get_card(auto=True)
        print(f"Player {mano.name} plays {card_mano}, player {pie.name} plays {card_pie}.")

        if card_mano.get_truco() < card_pie.get_truco():
            result[1] = mano
        if card_mano.get_truco() == card_pie.get_truco():
            result[1] = None
        else:
            result[1] = pie

        if result[1] == pie:
            mano, pie = pie, mano  # pie won, pie plays next

        if result[0] == result[1] and result[0] is not None:
            # update score and return
            round_winner = result[0]
            self.score[round_winner] += 1
            return

        # third
        if result[1] == player_2:
            mano, pie = player_2, player_1  # P2 won, P2 plays next
        card_mano = mano.get_card(auto=True)
        card_pie = pie.get_card(auto=True)
        print(f"Player {mano.name} plays {card_mano}, player {pie.name} plays {card_pie}.")

        if card_mano.get_truco() <= card_pie.get_truco():
            result[2] = mano
        else:
            result[2] = pie

        # update score and return
        p1, p2 = self.players
        if result.count(p1) >= result.count(p2):
            self.score[p1] += 1
        else:
            self.score[p2] += 1
        return
