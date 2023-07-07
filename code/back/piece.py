"""
    This is our class for pieces in game
"""


class Piece:

    def __init__(self, name, pos):
        self.name = name  # color + type --> (type) string
        self.pos = pos  # position on the board --> (type) tuple

    def valid_moves(self, board):  # where on the board piece can move
        pass
