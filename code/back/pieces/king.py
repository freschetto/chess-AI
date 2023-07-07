""""
    This class is our king type subclass of piece
"""

from code.back.piece import Piece


class King(Piece):

    def __init__(self, name, pos):
        super().__init__(name, pos)

    def valid_moves(self, board):

        valid_moves = []

        king_moves = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

        for move in king_moves:  # where on the board piece can move

            dx, dy = move
            x, y = self.pos[0] + dx, self.pos[1] + dy

            if 0 <= x < 8 and 0 <= y < 8:  # they must stay in the board

                if board.is_empty((x, y)) or board.is_enemy(self.name, (x, y)):
                    valid_moves.append((x, y))

        return valid_moves
