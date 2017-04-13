# Made by Jasque Saydyk and Miguel Quinones
# Lab 10 - Casino Night
# Section 2, April 12, 2017
# Description - Given code from the project to test Card and CardBank classes

from Card import *
from ChipBank import *
import random

if __name__ == "__main__":

    # Creates a list of cards to serve as the deck
    deck = []
    for i in range(52):
        my_card = Card(i)
        deck.append(my_card)
        # Flip over each card
        my_card.face_up()
        # Print each card as we add them
        print(my_card)

    # Print a random card from the deck
    print(random.choice(deck))

    # Using card number 37
    card = Card(37)
    print(card)
    # Queen of Clubs
    print(card.get_value())
    # 10
    print(card.get_suit())
    # Clubs
    print(card.get_rank())
    # Queen
    card.face_down()
    print(card)
    # <facedown>
    card.face_up()
    print(card)
    # Queen of Clubs

    cs = ChipBank(149)
    print(cs)
    # 1 blacks, 1 greens, 4 reds, 4 blues -- totaling $149
    cs.deposit(7)
    print(cs.get_balance())
    # 156
    print(cs)
    # 1 blacks, 2 greens, 1 reds, 1 blues -- totaling $156
    print(cs.withdraw(84))
    # 84
    print(cs)
    # 0 blacks, 2 greens, 4 reds, 2 blues -- totaling $72
    cs.deposit(120)
    print(cs)
    # 1 blacks, 3 greens, 3 reds, 2 blues -- totaling $192
    print(cs.withdraw(300))
    # 192
