from pawn import Pawn

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.pawns = [Pawn(color) for _ in range(4)]

    def move_pawn(self, board, pawn_index, spaces):
        self.pawns[pawn_index].move(board, spaces)

    def __str__(self):
        return f"Player {self.name} ({self.color}) with pawns: {', '.join(str(pawn) for pawn in self.pawns)}"
