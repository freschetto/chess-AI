"""
    This is our class for square in chess board
"""


class Square:

    def __init__(self, x, y):
        self.position = (x, y)  # where is the square
        self.proprieties = {
            "color": self.standard_color(x, y),
            "selected": False,
            "hover": False
        }

    @staticmethod
    def standard_color(row, col):  # this func() return color of square
        return (100, 100, 100) if (row + col) % 2 == 0 else (200, 200, 200)

    def change_color(self, action):
        self.proprieties[action] = True
        self.proprieties["color"] = (0, 200, 0) if self.proprieties["selected"] else (200, 200, 0)
