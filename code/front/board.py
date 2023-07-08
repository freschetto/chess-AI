
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

    def pick_mouse_square(self, pos):  # pick what square of the board we are with mouse
        return self.board[int(pos[1] / SQUARE_SIZE)][int(pos[0] / SQUARE_SIZE)]

    def selected_square(self, pos):  # change color and remove old square selected
        self.board[pos[1]][pos[0]].change_color("selected")
        for square in (sq for line in self.board for sq in line if sq.proprieties["selected"] and sq.pos != pos):
            square.color = square.standard_color(square.pos[1], square.pos[0])

    def draw(self, screen):  # draw every square in board
        for row, col, square in ((row, col, sq) for row, line in enumerate(self.board) for col, sq in enumerate(line)):
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, square.color, rect)

    def draw_pieces(self, screen, pieces):
        for piece in pieces:  # draw every pieces on board
            pos = (piece.pos[0] * SQUARE_SIZE, piece.pos[1] * SQUARE_SIZE)
            piece_image = pygame.transform.scale(self.pieces_images[piece.name], (SQUARE_SIZE, SQUARE_SIZE))
            screen.blit(piece_image, pos)  # load piece image in current self position
