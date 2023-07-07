"""
    This is our class for game engine function
"""

import code.back.board as b


class Game:

    def __init__(self):
        self.selected_piece = None
        self.board = b.Board()
        self.player = "w"

    def change_player(self):
        self.player = "b" if self.player == "w" else "w"

    def update(self):
        self.board.update()
        self.selected_piece = None
        self.change_player()

    # ------------------------------------------------------------------------------------------------------------------

    def user_input(self, x, y):

        if self.board.visual_board[y][x] != "  ":  # SELECT PIECE

            if self.selected_piece is None:  # PICK PIECE
                self.pick_piece((x, y))

            elif self.board.is_enemy(self.selected_piece.name, (x, y)) and self.valid_move((x, y)):  # ATTACK
                self.attack_enemy(self.selected_piece, (x, y))

            elif self.selected_piece.name[1] == "K" and self.board.visual_board[y][x][1] == "R":  # CASTLING
                pass

            else:  # CHANGE PIECE
                self.selected_piece = self.pick_piece((x, y))

        elif self.selected_piece is not None and self.valid_move((x, y)):  # MOVE
            self.move_piece(self.selected_piece, (x, y))

    # ------------------------------------------------------------------------------------------------------------------

    def valid_move(self, pos):
        return pos in self.selected_piece.valid_moves(self.board)

    def pick_piece(self, pos):  # if the user has not yet selected a piece --> piece(obj)
        return self.board.pick_piece(pos) if self.selected_piece.name[0] == self.player else None

    def attack_enemy(self, piece, pos):  # if we jet selected piece and want attack enemy piece
        self.board.remove_piece(pos)
        piece.pos = pos
        self.update()

    def move_piece(self, piece, pos):  # the pieces can move if square is empty and if we jet selected a piece
        piece.pos = pos
        self.update()

    # ------------------------------------------------------------------------------------------------------------------


game = Game()

print(".")
for value in game.board.visual_board:
    print(value)

game.selected_piece = game.board.pick_piece((1, 0))

game.move_piece(game.selected_piece, (0, 2))

print(".")
for value in game.board.visual_board:
    print(value)
