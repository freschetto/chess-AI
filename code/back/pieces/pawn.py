""""
    This class is our pawn type subclass of piece
"""

from code.back.piece import Piece


class Pawn(Piece):

    def __init__(self, name, pos):
        super().__init__(name, pos)
        self.start_position = pos

    def valid_moves(self, board):

        valid_moves = []

        dy = 1 if self.name[0] == "w" else -1
        x, y = self.pos[0], self.pos[1] + dy  # move one step forward

        if 0 <= x < 8 and 0 <= y < 8 and board.is_empty((x, y)):  # they must stay in the board

            valid_moves.append((x, y))

            if self.pos == self.start_position:  # move two steps forward from initial position

                x, y = self.pos[0], self.pos[1] + 2 * dy
                valid_moves.append((x, y)) if board.is_empty((x, y)) else None

        capture_moves = [(-1, dy), (1, dy)]  # pawn can capture diagonal

        for move in capture_moves:

            dx, dy = move
            x, y = self.pos[0] + dx, self.pos[1] + dy

            if 0 <= x < 8 and 0 <= y < 8 and board.is_enemy(self.name, (x, y)):

                valid_moves.append((x, y))

        return valid_moves
