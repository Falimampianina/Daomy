from collections import deque

from data_structures.playables.domino import Domino
from exceptions.exceptions import IllegalMove


class DominoSnake:
    def __init__(self, snake: deque[Domino] = deque()):
        self.snake = snake

    def _is_snake_empty(self) -> bool:
        if len(self.snake) == 0:
            return True
        else:
            return False

    def _get_front(self) -> int:
        return self.snake[0].left

    def _get_rear_end(self) -> int:
        return self.snake[-1].right

    def _get_ends(self) -> list[int]:
        return [self._get_front(), self._get_rear_end()]

    def check_if_domino_can_be_placed(self, domino: Domino) -> bool:
        if self._is_snake_empty():
            return True
        else:
            return domino.left in self._get_ends() or domino.right in self._get_ends()

    def place_domino(self, domino: Domino, position: str = None):
        if not self._is_snake_empty():
            if not self.check_if_domino_can_be_placed(domino):
                raise IllegalMove()
            else:
                if not position:
                    if domino.left == self._get_front():
                        self.snake.appendleft(domino.reverse())
                    elif domino.left == self._get_rear_end():
                        self.snake.append(domino)
                    elif domino.right == self._get_front():
                        self.snake.appendleft(domino)
                    elif domino.right == self._get_rear_end():
                        self.snake.append(domino.reverse())
                else:
                    if position == "front":
                        if domino.right != self._get_front():
                            self.snake.appendleft(domino.reverse())
                        else:
                            self.snake.appendleft(domino)
                    elif position == "rear":
                        if domino.left != self._get_rear_end():
                            self.snake.append(domino.reverse())
                        else:
                            self.snake.append(domino)
        else:
            self.snake.append(domino)

    def __str__(self):
        output = "Actual snake: "
        for domino in self.snake:
            output += str(domino) + " "
        return output
