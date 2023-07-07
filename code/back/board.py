"""
    This is our class for game chess board
"""

from code.back.pieces.king import King
from code.back.pieces.queen import Queen
from code.back.pieces.rook import Rook
from code.back.pieces.bishop import Bishop
from code.back.pieces.knight import Knight
from code.back.pieces.pawn import Pawn


class Board:

    def __init__(self):
        self.visual_board = []  # create an empty game board
        self.pieces_on_board = self.create_pieces()  # create every piece in game
        self.update()  # update all pieces on board

    '''
            Board indexes for user reference:
        
            [0,0]   [1,0]   [2,0]   [3,0]   [4,0]   [5,0]   [6,0]   [7,0]
            [0,1]   [1,1]   [2,1]   [3,1]   [4,1]   [5,1]   [6,1]   [7,1]
            [0,2]   [1,2]   [2,2]   [3,2]   [4,2]   [5,2]   [6,2]   [7,2]
            [0,3]   [1,3]   [2,3]   [3,3]   [4,3]   [5,3]   [6,3]   [7,3]
            [0,4]   [1,4]   [2,4]   [3,4]   [4,4]   [5,4]   [6,4]   [7,4]
            [0,5]   [1,5]   [2,5]   [3,5]   [4,5]   [5,5]   [6,5]   [7,5]
            [0,6]   [1,6]   [2,6]   [3,6]   [4,6]   [5,6]   [6,6]   [7,6]
            [0,7]   [1,7]   [2,7]   [3,7]   [4,7]   [5,7]   [6,7]   [7,7]
    '''

    @staticmethod
    def empty_board(size_board):  # create and clear the game board
        return [['  ' for _ in range(size_board)] for _ in range(size_board)]

    @staticmethod
    def create_pieces():

        pieces = []  # create piece for each type (subclass) and team (white,black) --> (type) list[obj]
        for value in ('P', 'R', 'B', 'N', 'Q', 'K'):

            for color in ('w', 'b'):

                if value == 'K':  # king
                    pieces.append(King(color + value, (4, 0) if color == 'w' else (4, 7)))

                elif value == 'Q':  # queen
                    pieces.append(Queen(color + value, (3, 0) if color == 'w' else (3, 7)))

                elif value == 'R':  # rook
                    pieces.append(Rook(color + value, (0, 0) if color == 'w' else (0, 7)))
                    pieces.append(Rook(color + value, (7, 0) if color == 'w' else (7, 7)))

                elif value == 'N':  # knight
                    pieces.append(Knight(color + value, (1, 0) if color == 'w' else (1, 7)))
                    pieces.append(Knight(color + value, (6, 0) if color == 'w' else (6, 7)))

                elif value == 'B':  # bishop
                    pieces.append(Bishop(color + value, (2, 0) if color == 'w' else (2, 7)))
                    pieces.append(Bishop(color + value, (5, 0) if color == 'w' else (5, 7)))

                elif value == 'P':  # pawn
                    for index in range(8):
                        pieces.append(Pawn(color + value, (index, 1) if color == 'w' else (index, 6)))
        return pieces

    # ------------------------------------------------------------------------------------------------------------------

    def pick_piece(self, pos):  # if exist pick piece on the board (position)
        return next((piece for piece in self.pieces_on_board if piece.pos == pos), None)

    def remove_piece(self, pos):  # remove piece on the board
        self.pieces_on_board.remove(self.pick_piece(pos))

    # ------------------------------------------------------------------------------------------------------------------

    def is_empty(self, pos) -> bool:  # can move if destination is empty
        return self.visual_board[pos[1]][pos[0]] == '  '

    def is_enemy(self, name_piece, pos) -> bool:  # can capture enemy's piece
        return self.visual_board[pos[1]][pos[0]][0] != name_piece[0] and not self.is_empty(pos)

    # ------------------------------------------------------------------------------------------------------------------

    def update(self):  # pick one by one all piece to load on board
        self.visual_board = self.empty_board(8)
        for piece in self.pieces_on_board:
            self.visual_board[piece.pos[1]][piece.pos[0]] = piece.name
