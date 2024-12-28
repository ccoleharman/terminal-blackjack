import random
from .card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()
        self.shuffle_deck()

    def build_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for _ in range(6):
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(suit, rank))

    def len(self):
        return len(self.cards)

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

    def __repr__(self):
        return '\n'.join(str(card) for card in self.cards)
