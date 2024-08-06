class Pawn:
    def __init__(self, color):
        self.color = color
        self.position = 'START'

    def move(self, spaces):
        if self.position == 'START':
            if spaces == 1 or spaces == 2:
                self.position = 1  # Start on the board at position 1
        else:
            self.position += spaces

    def __str__(self):
        return f"Pawn({self.color}, position: {self.position})"
