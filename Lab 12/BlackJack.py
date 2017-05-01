# Made by Jasque Saydyk and Ian Otto
# Lab 12 - Blackjack
# Section 2, May 1, 2017
# Description - Blackjack class to conduct the game of Blackjack
import random
from BlackjackHand import *
from ChipBank import *
from Card import *


class Blackjack:

    def __init__(self, starting_dollars):
        """
        Creates a new Blackjack games in which the player starts with 'starting_dollars'
        worth of money. This method will need to set up instance variables to support
        the rest of the game. This should initialize the deck, and the player's chip stack.
        Remember to shuffle the deck after you create it.
        :param starting_dollars:
        """
        self._active = False
        self._chipbank = ChipBank(starting_dollars)
        self._deck = self.build_deck()
        self._player_hand = BlackjackHand()
        self._dealer_hand = BlackjackHand()
        self._wager = 0

    def build_deck(self):
        """
        Makes deck of cards for class to use
        """
        deck = []
        for i in range(52):
            my_card = Card(i)
            deck.append(my_card)
        random.shuffle(deck)
        return deck

    def draw(self):
        """
        This method draws and returns a card from the deck. If the deck is empty when
        this method is called, rebuild and reshuffle the deck. Make sure that all cards
        are drawn face up. Return a card object after it is removed from the deck.
        :return: Card A Card object removed from the deck.
        """
        # Deck returns a False if it is empty,
        if self._deck:
            card = self._deck[0]
            del (self._deck[0])
        else:
            self._deck = self.build_deck()
            card = self._deck[0]
            del (self._deck[0])
        return card

    def get_bank_amt(self):
        """
        :return: The current chipbank of the game
        """
        return self._chipbank

    def start_hand(self, wager):
        """
        Starts a new hand of blackjack. Should initialize instance variables with a
        new hand for the player and the dealer. Remember that the first dealer's card
        should be set face down. This object should withdraw the wager amount from
        the ChipBank, and remember that value for the end of the game. Print both
        the player's hand and the dealer's hand to the player, and check to see if the
        player wins automatically with blackjack. If both the player AND the dealer
        have 21, it is a tie, or push.
        :param wager: Numeric value representing the bet placed on the hand.
        """
        self._active = True
        self._wager = wager
        self._chipbank.withdraw(wager)

        self._player_hand.add_card(self.draw())
        self._player_hand.add_card(self.draw())
        print("your starting hand: " + str(self._player_hand))
        fd_card = self.draw()
        fd_card.face_down()
        self._dealer_hand.add_card(self.draw())
        self._dealer_hand.add_card(fd_card)
        print("dealer's hand: " + str(self._dealer_hand))

    def hit(self):
        """
        The player chooses to hit. Draw a card for the player, and display the player's
        new hand. If they exceed 21 they bust, and if they get 21 exactly they are forced
        to stand. This method takes no parameters, and has no return value.
        """
        card = self.draw()
        self._player_hand.add_card(card)
        print("drew a " + str(card))
        print("player's hand: " + str(self._player_hand))
        if self._player_hand.get_value() > 21:
            print("player busts")
            self.stand()

    def stand(self):
        """
        The player stands, and the dealer ips their hidden card face up and begins the
        process of drawing. The dealer only draws if their hands current value is 16 or
        less. If the dealer draws over 21, they bust and the player wins. After the dealer
        is done drawing, and neither has busted, the higher valued hand wins. Ties can
        occur, and are called "pushes".
        """
        self._dealer_hand.face_up_all()
        print("player's hand: " + str(self._player_hand))

        while self._dealer_hand.get_value() <= 16:
            card = self.draw()
            print("drew a " + str(card))
            self._dealer_hand.add_card(card)

        if self._dealer_hand.get_value() == self._player_hand.get_value():
            self.end_hand("push")
        elif self._dealer_hand.get_value() > 21 and self._player_hand.get_value() > 21:
            self.end_hand("push")
        elif self._dealer_hand.get_value() > 21:
            self.end_hand("win")
        elif self._player_hand.get_value() > 21:
            self.end_hand("lose")
        elif self._dealer_hand.get_value() > self._player_hand.get_value():
            self.end_hand("lose")
        else:
            self.end_hand("win")

    def end_hand(self, outcome):
        """
        This method should be called when a winner has been determined. This method
        is passed a parameter outcome, which will be win, lose, or push depending
        on if the player won, the dealer won, or their was a tie. If the player wins they
        should be given double their wager back. A push should refund the original
        wager, and a lose should result in no money being deposited. This method is
        also responsible for setting the two hands and the wager back to None
        :param outcome: A string containing either "win", "lose", or "push"
        """
        self._active = False
        if outcome == "push":
            self._chipbank.deposit(self._wager)
        elif outcome == "lose":
            print("lose")
        else:
            self._chipbank.deposit(self._wager * 2)

    def game_active(self):
        """
        Returns True or False, indicating if there is a current hand in play. Should
        return True when start_hand() has been called, and end_hand() has not yet
        been called to close the game.
        :return: Returns a boolean value, True or False, depending on if there is an active hand
            that has not yet been resolved.
        """
        return self._active
