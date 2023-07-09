
import pygame

from code.front.square import Square
from code.front.constant import BOARD_X, BOARD_Y, SQUARE_SIZE


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
        return self.board[int((pos[1] - BOARD_Y) / SQUARE_SIZE)][int((pos[0] - BOARD_X) / SQUARE_SIZE)]

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
    def draw_board(screen, board):
        for row, col, square in ((row, col, sq) for row, line in enumerate(board) for col, sq in enumerate(line)):
            rect = pygame.Rect(col * SQUARE_SIZE + BOARD_X, row * SQUARE_SIZE + BOARD_Y, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, square.color, rect)

    @staticmethod
    def draw_pieces(images, screen, pieces):
        for piece in pieces:  # draw every pieces on board
            pos = (piece.pos[0] * SQUARE_SIZE + BOARD_X, piece.pos[1] * SQUARE_SIZE + BOARD_Y)
            piece_image = pygame.transform.scale(images[piece.name], (SQUARE_SIZE, SQUARE_SIZE))
            screen.blit(piece_image, pos)  # load piece image in current self position

    @staticmethod
    def show_possible_moves(screen, board, piece):
        for move in piece.valid_moves(board):
            pos = ((move[0] * SQUARE_SIZE + BOARD_X) + SQUARE_SIZE / 2, (move[1] * SQUARE_SIZE + BOARD_Y) + SQUARE_SIZE / 2)
            pygame.draw.circle(screen, (0, 200, 0), pos, 10)

    # ------------------------------------------------------------------------------------------------------------------

    def draw(self, screen, board, piece):  # draw every square in board

        self.draw_board(screen, self.board)

        self.draw_pieces(self.pieces_images, screen, board.pieces_on_board)

        self.show_possible_moves(screen, board, piece) if piece is not None else None
