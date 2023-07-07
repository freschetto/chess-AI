""""
    This class is our rook type subclass of piece
"""

from code.back.piece import Piece


class Rook(Piece):

    def __init__(self, name, pos):
        super().__init__(name, pos)

    def valid_moves(self, board):

        valid_moves = []

        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # where on the board piece can move

            dx, dy = direction
            x, y = self.pos[0] + dx, self.pos[1] + dy

            while 0 <= x < 8 and 0 <= y < 8:  # they must stay in the board

                if board.is_empty((x, y)):  # if empty it can move
                    valid_moves.append((x, y))

                elif board.is_enemy(self.name, (x, y)):  # rook can capture if there is an enemy
                    valid_moves.append((x, y))
                    break

                else:  # check if the possible moves are not obstructed
                    break

                x += dx
                y += dy

        return valid_moves
