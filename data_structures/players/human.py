from data_structures.playables.domino import Domino
from data_structures.playables.dominoes_set import DominoesSet
from data_structures.players.player import Player


class Human(Player):
    def __init__(self, name: str = None, score: int = 0, dominoes: list[Domino] = None):
        super().__init__(name, score, dominoes)

    def play(self):
        pass
