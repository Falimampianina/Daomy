class Domino:
    """
        Domino class is used to represent a domino
        parameters:
            -left: an integer representing the left side of the domino 0 to 6
            -right: an integer representing the right side of the domino 0 to 6
    """
    def __init__(self, left: int, right: int):
        if left < 0 or right < 0 or left > 6 or right > 6:
            raise ValueError("Domino's number must be between 0 and 6 (both included).")
        else:
            self.left = left
            self.right = right

    @property
    def left(self) -> int:
        return self._left

    @left.setter
    def left(self, value: int):
        self._left = value

    @property
    def right(self) -> int:
        return self._right

    @right.setter
    def right(self, value: int):
        self._right = value

    def __str__(self):
        return "[" + str(self.left) + " | " + str(self.right) + "]"

    def __eq__(self, other) -> bool:
        return ((self.left == other.left and self.right == other.right) or
                (self.left == other.right and self.right == other.left))

    def reverse(self):
        self.right, self.left = self.left, self.right
        return self
