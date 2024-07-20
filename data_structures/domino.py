class Domino:
    """
        Domino class is used to represent a domino
        parameters:
            -left: an integer representing the left side of the domino 0 to 6
            -right: an integer representing the right side of the domino 0 to 6
    """
    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right

    def __str__(self):
        return "[" + str(self.left) + " | " + str(self.right) + "]"

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def reverse(self):
        self.right, self.left = self.left, self.right
