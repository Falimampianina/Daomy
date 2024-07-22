from data_structures.playables.domino import Domino
from data_structures.playables.domino_snake import DominoSnake


class Player:
    def __init__(self, name: str = None, score: int = 0, dominoes: list[Domino] = None):
        self.name = name
        self.score = score
        self.dominoes = dominoes

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, score: int):
        self._score = score

    @property
    def dominoes(self) -> list[Domino]:
        return self._dominoes

    @dominoes.setter
    def dominoes(self, other_dominoes: list[Domino]):
        self._dominoes = other_dominoes

    def increase_score(self, score: int):
        self._score += score

    def all_dominoes_placed(self) -> bool:
        if len(self.dominoes) == 0:
            return True
        return False

    def useless_hand(self, snake: DominoSnake) -> bool:
        return all([not snake.check_if_domino_can_be_placed(domino) for domino in self.dominoes])

    def get_total_weight_of_remaining_dominoes(self) -> int:
        total = 0
        for domino in self.dominoes:
            total += domino.get_weight()
        return total

    def __str__(self):
        output = f"{self.name} score: {self.score}\nDominoes:\n"
        for domino in self.dominoes:
            output += str(domino) + "\n"
        return output
