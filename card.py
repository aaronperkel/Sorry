class Card:
    def __init__(self, value, description):
        self.value = value
        self.description = description

    def __str__(self):
        return f"{self.value}: {self.description}"
