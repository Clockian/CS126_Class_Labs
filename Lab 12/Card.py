# Made by Jasque Saydyk and Ian Otto
# Lab 12 - Blackjack
# Section 2, May 1, 2017
# Description - Represents a basic, western playing card


class Card:

    _face = False
    _suit = "None"
    _name = "None"
    _value = 0

    def __init__(self, card_num):
        """
        Initializes class variables
        :param card_num - An int between 0 and 51, indicating which card in
            the deck it is. For this project, first 13 will represent Ace of
            Spades to King of Spades, next 13 is Ace of Hearts to King of
            Hearts, and so forth
        """
        self._card_num = card_num + 1
        self.auto_assign_name_and_suit()

    def auto_assign_name_and_suit(self):
        """
        Intended for internal class use only
        Auto assigns the variables below based on the card_num given
        card_suit - Represents the suit of the card, either Heart, Spade,
            Clover, and Diamond
        card_rank - The rank of the card, Ace, Jack, Queen, or King
        """
        # Uses card's number to find its Suit
        if self._card_num <= 13:
            self._suit = 'Spades'
        elif self._card_num <= 26:
            self._suit = 'Hearts'
        elif self._card_num <= 39:
            self._suit = 'Clubs'
        elif self._card_num <= 52:
            self._suit = 'Diamonds'

        # Uses the card's number to find its face/value
        self._name = self._card_num % 13
        if self._name == 1:
            self._name = 'Ace'
            self._value = 11
        elif self._name == 11:
            self._name = 'Jack'
            self._value = 10
        elif self._name == 12:
            self._name = 'Queen'
            self._value = 10
        elif self._name == 0:
            self._name = 'King'
            self._value = 10
        else:
            self._value = self._name

    def get_suit(self):
        """
        :return String representing the suit of the card, Spades, Clovers,
            Clubs, Hearts
        """
        return self._suit

    def get_rank(self):
        """
        :return String representing rank of the card, Aces, Jack, Queen,
            King, or number of the card
        """
        return str(self._name)

    def get_value(self):
        """
        :return String representing value of the card between 0 to 51
        """
        return self._value

    def face_down(self):
        """
        Method flips the card face-down, cards are face-down by default.
            False is equivalent to down
        """
        self._face = False

    def face_up(self):
        """
        Method flips hidden cards face-up, making them no longer hidden.
            True is equivalent to up
        """
        self._face = True

    def __str__(self):
        """
        :return String representation of the card, if the card is face-up
            returns "5 of Diamonds", if the card is face down, returns
            "<facedown>"
        """
        if not self._face:
            return "<facedown>"
        else:
            return str(self._name) + " of " + self._suit
