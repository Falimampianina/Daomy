from unittest import TestCase

from data_structures.playables.domino import Domino
from data_structures.playables.domino_snake import DominoSnake
from exceptions.exceptions import IllegalMove


class TestDominoSnake(TestCase):
    def setUp(self):
        self.d_snake = DominoSnake()
        self.d_snake.place_domino(Domino(0, 0))
        self.d_snake.place_domino(Domino(0, 1))

    def test_place_domino(self):
        self.assertIn(Domino(0, 0), self.d_snake.snake)
        self.assertIn(Domino(1, 0), self.d_snake.snake)

    def test_illegal_move(self):
        with self.assertRaises(IllegalMove):
            self.d_snake.place_domino(Domino(2, 5))
