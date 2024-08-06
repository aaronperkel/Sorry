import pygame as pg

class Board:
    def __init__(self):
        self.board_positions = [[1] * 16] + [[1] + [0] * 14 + [1] for _ in range(14)] + [[1] * 16]
        self.squares = []
        self.createSquares()

    def createSquares(self):
        screen_size = 900
        grid_size = len(self.board_positions)
        padding = 12
        available_space = screen_size - 2 * padding
        square_size = available_space // grid_size
        xLoc, yLoc = padding, padding
        for row in self.board_positions:
            xLoc = padding
            for element in row:
                if element == 1:
                    self.squares.append(pg.Rect(xLoc, yLoc, square_size, square_size))
                xLoc += square_size
            yLoc += square_size



    def move_pawn(self, pawn, spaces):
        current_pos = pawn.position

        if current_pos == 'START':
            if spaces in [1, 2]:  # Only move out of start if 1 or 2 is drawn
                new_pos = 0  # Start on the board at position 0
            else:
                print(f"{pawn.color} pawn stays at START.")
                return  # No movement, stays at START
        else:
            # Ensure current_pos is an integer before performing arithmetic
            new_pos = (int(current_pos) + spaces) % len(self.board_positions)

        # Handle collision and bumping
        if self.board_positions[new_pos] is not None:
            bumped_pawn = self.board_positions[new_pos]
            bumped_pawn.position = 'START'
            print(f"Bumped {bumped_pawn.color} pawn back to START!")

        # Update board positions
        if current_pos != 'START':  # Don't clear 'START'
            self.board_positions[current_pos] = None  # Clear old position
        self.board_positions[new_pos] = pawn  # Set new position
        pawn.position = new_pos

    def __str__(self):     
        return '\n'.join(' '.join(map(str, row)) for row in self.board_positions)
