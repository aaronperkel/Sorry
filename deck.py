from card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        card_data = [
            (1, "Move from Start or move forward 1.", 5),
            (2, "Move from Start or move forward 2. DRAW AGAIN.", 4),
            (3, "Move forward 3.", 4),
            (4, "Move backward 4.", 4),
            (5, "Move forward 5.", 4),
            (7, "Move forward 7 or split between two pawns.", 4),
            (8, "Move forward 8.", 4),
            (10, "Move forward 10 or move backward 1.", 4),
            (11, "Move forward 11 or change places with an opponent.", 4),
            (12, "Move forward 12.", 4),
            ("SORRY!", "Move from Start and switch places with an opponent.", 4)
        ]
        for value, description, quantity in card_data:
            for _ in range(quantity):
                self.cards.append(Card(value, description))
        random.shuffle(self.cards)

    def draw_card(self):
        if not self.cards:
            self.build_deck()
        return self.cards.pop(0)
