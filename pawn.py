class Pawn:
    def __init__(self, color):
        self.color = color
        self.position = 'START'

    def move(self, board, spaces):
        board.move_pawn(self, spaces)

    def __str__(self):
        return f"Pawn({self.color}, position: {self.position})"