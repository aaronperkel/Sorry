from deck import Deck
from player import Player
from board import Board
import time
import pygame as pg
import sys

pg.init()
pg.display.set_caption('Sorry!')

class Game:
    def __init__(self):
        SCREEN_SIZE = (900, 900)
        self.BACKGROUND_COLOR = (122, 173, 255)

        self.screen = pg.display.set_mode(SCREEN_SIZE)

        self.players = []
        self.deck = Deck()
        self.board = Board()
        self.setup_game()

    def setup_game(self):
        player_colors = ['Red', 'Yellow', 'Green', 'Blue']

    def play_turn(self, player):
        # Add logic to select a pawn and move it based on the card drawn
        # Example: for now, just move the first pawn
        card = self.deck.draw_card()
        player.move_pawn(self.board, 0, card.value)  # Basic movement logic
        print(self.board)

    def play_game(self):
        game_over = False
        while not game_over:
            self.screen.fill(self.BACKGROUND_COLOR)
            keys = pg.key.get_pressed() 

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            for rect in self.board.squares:
                pg.draw.rect(self.screen, (255, 255, 255), rect, 0, 6)

            pg.display.update()

if __name__ == "__main__":
    game = Game()
    game.play_game()
