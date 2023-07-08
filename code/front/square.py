"""
    This is our class for square in chess board
"""

from code.front.constant import SQUARE_COLOR


class Square:

    def __init__(self, x, y):
        self.pos = (x, y)  # where is the square
        self.proprieties = {"selected": False, "hover": False, "checkmate": False}
        self.color = self.standard_color(x, y)

    def standard_color(self, row, col):  # this func() return color of square
        self.proprieties = {key: False for key in self.proprieties}
        return SQUARE_COLOR["BLACK"] if (row + col) % 2 == 0 else SQUARE_COLOR["WHITE"]

    def change_color(self, action):
        self.proprieties[action] = True
        self.color = SQUARE_COLOR[action.upper()]
