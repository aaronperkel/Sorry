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

    def play_game(self):
        game_over = False
        while not game_over:
            self.screen.fill(self.BACKGROUND_COLOR)
            keys = pg.key.get_pressed() 

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            for rect, element in self.board.squares:
                if element == 1:
                    pg.draw.rect(self.screen, (188, 192, 219), (rect[0] - 8, rect[1] - 8, rect[2] + 16, rect[3] + 16), 0, 6)

            for rect, element in self.board.squares:
                match element:
                    case 1:
                        color = (229, 232, 246)
                    case 2 | 6:
                        color = (214, 213, 69)
                    case 3 | 7:
                        color = (108, 161, 66)
                    case 4 | 8:
                        color = (70, 156, 235)
                    case 5 | 9:
                        color = (195, 43, 47)
                    case _:
                        color = (0, 0, 0)
                if element in [1, 2, 3, 4, 5]:
                    pg.draw.rect(self.screen, color, rect, 0, 6)
                else:
                    pg.draw.circle(self.screen, color, (rect[0] + (rect[2] // 2), rect[1] + rect[3]), 64)

            pg.display.update()

if __name__ == "__main__":
    game = Game()
    game.play_game()
