
import sys
import pygame

from code.back.game import Game
from code.front.board import Board
from code.front.constant import DISPLAY_WIDTH, DISPLAY_HEIGHT


class Surface:

    def __init__(self):
        self.game = Game()  # BACKEND
        self.screen = self.set_display()
        self.board = Board(self.game.board.pieces_on_board)  # GRAPHIC BOARD

    @staticmethod  # SET DISPLAY
    def set_display():

        # standard settings
        screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        screen.fill((255, 255, 255))

        # change screen logo image
        logo_image = pygame.image.load("front/images/bR.png")
        logo_image = pygame.transform.scale(logo_image, (32, 32))
        pygame.display.set_icon(logo_image)

        # set the title of the window
        pygame.display.set_caption("...")

        return screen

    # ------------------------------------------------------------------------------------------------------------------

    def draw(self):  # DRAW ALL THINGS

        self.board.draw(self.screen, self.game.board, self.game.selected_piece)

        pygame.display.flip()  # flip() the display to put your work on screen

    def update(self):

        self.draw()

        for event in pygame.event.get():

            square = self.board.pick_mouse_square(pygame.mouse.get_pos())

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                self.board.selected_square(square)

                self.game.user_input(square.pos)  # UPDATE BACKEND

            elif event.type == pygame.MOUSEMOTION and not square.proprieties["selected"]:

                self.board.hover_square(self.game.board.visual_board[square.pos[1]][square.pos[0]], square)
