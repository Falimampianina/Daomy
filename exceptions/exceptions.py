class IllegalMove(Exception):
    def __init__(self, message="This domino can't be placed on the snake"):
        super().__init__(message)
