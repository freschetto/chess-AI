
import pygame

from code.front.square import Square
from code.front.constant import BOARD_SIZE, SQUARE_SIZE


class Board:

    def __init__(self, pieces):
        self.board = self.load_board()
        self.pieces_images = self.load_pieces(pieces)

    @staticmethod
    def load_board():  # load visual square
        return [[Square(x, y) for x in range(8)] for y in range(8)]

    @staticmethod
    def load_pieces(pieces):
        return {piece.name: pygame.image.load("front/images/" + piece.name + ".png") for piece in pieces}

    # ------------------------------------------------------------------------------------------------------------------

    def pick_mouse_square(self, pos):  # pick what square of the board we are with mouse
        return self.board[int(pos[1] / SQUARE_SIZE)][int(pos[0] / SQUARE_SIZE)]

    def selected_square(self, square):  # change color and remove old square selected
        square.change_color("selected")
        for sq in (sq for line in self.board for sq in line if sq.proprieties["selected"] and sq.pos != square.pos):
            sq.color = sq.standard_color("selected", sq.pos[0], sq.pos[1])

    def hover_square(self, content, square):  # change color and remove old square hover
        square.change_color("hover") if content != '  ' else None
        for sq in (sq for line in self.board for sq in line if sq.proprieties["hover"] and sq.pos != square.pos):
            if not sq.proprieties["selected"]:
                sq.color = sq.standard_color("hover", sq.pos[0], sq.pos[1])

    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def show_possible_moves(screen, board, piece):
        for move in piece.valid_moves(board):
            pygame.draw.circle(screen, (0, 200, 0), ((move[0] * SQUARE_SIZE) + SQUARE_SIZE / 2,
                                                     (move[1] * SQUARE_SIZE) + SQUARE_SIZE / 2), 10)

    def draw_pieces(self, screen, pieces):
        for piece in pieces:  # draw every pieces on board
            pos = (piece.pos[0] * SQUARE_SIZE, piece.pos[1] * SQUARE_SIZE)
            piece_image = pygame.transform.scale(self.pieces_images[piece.name], (SQUARE_SIZE, SQUARE_SIZE))
            screen.blit(piece_image, pos)  # load piece image in current self position

    # ------------------------------------------------------------------------------------------------------------------

    def draw(self, screen, board, piece):  # draw every square in board

        for row, col, square in ((row, col, sq) for row, line in enumerate(self.board) for col, sq in enumerate(line)):
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, square.color, rect)

        self.draw_pieces(screen, board.pieces_on_board)
        self.show_possible_moves(screen, board, piece) if piece is not None else None
