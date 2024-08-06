from deck import Deck
from player import Player
import time

class Game:
    def __init__(self):
        self.players = []
        self.deck = Deck()
        self.setup_game()

    def setup_game(self):
        player_colors = ['Red', 'Yellow', 'Green', 'Blue']

        print('\n\nWelcome to SORRY!')
        print('=============================================\n\n')

        while True:
            num_players = int(input("Enter the number of players (2-4): "))
            if num_players in [2, 3, 4]:
                break
            else:
                print("Invalid number of players. Please enter 2, 3, or 4.")

        for i in range(num_players):
            name = input(f"Enter player {i + 1} name: ")
            color = player_colors[i]
            self.players.append(Player(name, color))

    def play_turn(self, player):
        print(f"\n{player.name}'s turn:")
        input("Press 'Enter' to draw a card!")
        card = self.deck.draw_card()
        print(f"Drawn card: {card}")
        print('=====================================')
        time.sleep(3)
        
        # Add logic to move pawns based on the card
        # Prompt the player for which pawn to move

    def play_game(self):
        game_over = False
        while not game_over:
            for player in self.players:
                self.play_turn(player)
                # Check for game-winning condition

if __name__ == "__main__":
    game = Game()
    game.play_game()
