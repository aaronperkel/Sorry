class Board:
    def __init__(self):
        # Initialize the board positions
        self.board_positions = [None] * 60  # Example: a circular board with 60 positions

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
        return "Board positions: " + str(self.board_positions)
