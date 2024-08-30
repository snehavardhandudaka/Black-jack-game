# game.py
from deck import Deck
from player import Player
from dealer import Dealer

def play_game():
    deck = Deck()
    player = Player("Player", 100)
    dealer = Dealer()

    # Initial dealing
    player.hand.add_card(deck.deal())
    player.hand.add_card(deck.deal())
    dealer.hand.add_card(deck.deal())
    dealer.hand.add_card(deck.deal())

    # Player's turn
    while True:
        print(f"Player's hand: {[str(card) for card in player.hand.cards]}, value: {player.hand.value}")
        if player.hand.value > 21:
            player.hand.adjust_for_ace()
        if player.hand.value > 21:
            print("Player busts!")
            break
        action = input("Do you want to hit or stand? (h/s): ")
        if action == 'h':
            player.hand.add_card(deck.deal())
        else:
            break

    # Dealer's turn
    while dealer.hand.value < 17:
        dealer.hand.add_card(deck.deal())
        if dealer.hand.value > 21:
            dealer.hand.adjust_for_ace()

    # Determine winner
    print(f"Dealer's hand: {[str(card) for card in dealer.hand.cards]}, value: {dealer.hand.value}")
    if dealer.hand.value > 21 or player.hand.value > dealer.hand.value:
        print("Player wins!")
        player.win(10)
    elif player.hand.value < dealer.hand.value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
