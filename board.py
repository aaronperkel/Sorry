import pygame as pg

class Board:
    def __init__(self):
        self.board_positions = [[1] * 16] + [[1] + [0] * 14 + [1] for _ in range(14)] + [[1] * 16]
        self.squares = []
        self.create_zones()
        self.create_squares()

    def create_squares(self):
        screen_size = 900
        grid_size = len(self.board_positions)
        padding = 12
        available_space = screen_size - 2 * padding
        square_size = available_space // grid_size
        xLoc, yLoc = padding, padding
        for row in self.board_positions:
            xLoc = padding
            for element in row:
                if element != 0:
                    self.squares.append((pg.Rect(xLoc, yLoc, square_size, square_size), element))
                xLoc += square_size
            yLoc += square_size

    def create_zones(self):
        for col in range(1, 6):
            self.board_positions[col][2] = 2
        self.board_positions[6][2] = 6
        self.board_positions[1][4] = 6

        for row in range(10, 15):
            self.board_positions[2][row] = 3

        for row in range(1, 6):
            self.board_positions[13][row] = 4

        for col in range(10, 15):
            self.board_positions[col][13] = 5

    def move_pawn(self):
        pass

    def __str__(self):     
        return '\n'.join(' '.join(map(str, row)) for row in self.board_positions)
