# player.py
from hand import Hand

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand = Hand()

    def bet(self, amount):
        self.money -= amount

    def win(self, amount):
        self.money += amount
