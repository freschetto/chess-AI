""""
    This class is our knight type subclass of piece
"""

from code.back.piece import Piece


class Knight(Piece):

    def __init__(self, name, pos):
        super().__init__(name, pos)

    def valid_moves(self, board):

        valid_moves = []

        knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        for move in knight_moves:  # where on the board piece can move

            dx, dy = move
            x, y = self.pos[0] + dx, self.pos[1] + dy

            if 0 <= x < 8 and 0 <= y < 8:  # they must stay in the board

                if board.is_empty((x, y)) or board.is_enemy(self.name, (x, y)):
                    valid_moves.append((x, y))

        return valid_moves
