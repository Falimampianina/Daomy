import random

from data_structures.playables.domino import Domino
from data_structures.playables.domino_snake import DominoSnake
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

    def _ai_make_random_legal_move(self, snake: DominoSnake):
        playable_pieces = []
        for domino in self.dominoes:
            if snake.check_if_domino_can_be_placed(domino):
                playable_pieces.append(domino)
        chosen_piece = random.choice(playable_pieces)
        snake.place_domino(chosen_piece)
        self.dominoes.remove(chosen_piece)

    def play(self, snake: DominoSnake):
        if self.useless_hand(snake):
            return
        else:
            if self.level == 0:
                self._ai_make_random_legal_move(snake)
