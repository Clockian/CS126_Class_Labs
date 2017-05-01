# Made by Jasque Saydyk and Ian Otto
# Lab 12 - Blackjack
# Section 2, May 1, 2017
# Description - Given code from the project to test Blackjack classes
from Blackjack import *

if __name__ == "__main__":
    blackjack = Blackjack(250)
    while blackjack.bank.value > 0:
        print("Your remaining chips: " + str(blackjack.bank))
        wager = int(input("How much would you like to wager? "))
        blackjack.start_hand(wager)
        while blackjack.game_active():
            choice = input("STAND or HIT: ").upper()
            if choice == "STAND":
                blackjack.stand()
            elif choice == "HIT":
                blackjack.hit()
        print()
    print("Out of money! The casino wins!")
