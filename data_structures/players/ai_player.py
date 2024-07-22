from data_structures.playables.domino import Domino
from data_structures.players.player import Player


class AIPlayer(Player):
    def __init__(self, name: str = None, score: int = 0, dominoes: list[Domino] = None, level: int = 0):
        super().__init__(name, score, dominoes)
        self.level = level

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, value: int):
        self._level = value
