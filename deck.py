# deck.py
import random
from card import Card

class Deck:
    suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self):
        self.deck = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
