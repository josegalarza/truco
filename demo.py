from src.game import Game
from src.player import Player


p1 = Player('Jose')
p2 = Player('Fran')

g = Game(players=[p1, p2])
g.play()
