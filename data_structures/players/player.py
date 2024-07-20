from abc import ABC, abstractmethod

from data_structures.playables.domino import Domino


class Player(ABC):
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

    def __str__(self):
        output = f"{self.name} score: {self.score}\nDominoes:\n"
        for domino in self.dominoes:
            output += str(domino) + "\n"
        return output

    @abstractmethod
    def play(self):
        pass
