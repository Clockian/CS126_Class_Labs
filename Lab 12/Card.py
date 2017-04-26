# Made by Jasque Saydyk and Miguel Quinones
# Lab 10 - Casino Night
# Section 2, April 12, 2017
# Description - Represents a basic, western playing card


class Card:

    card_face = False
    card_rank = "None"
    card_suit = "None"

    def __init__(self, card_num):
        """
        Initializes class variables
        :param card_num - An int between 0 and 51, indicating which card in
            the deck it is. For this project, first 13 will represent Ace of
            Spades to King of Spades, next 13 is Ace of Hearts to King of
            Hearts, and so forth
        """
        self.card_num = card_num
        self.auto_assign_rank_and_suit()

    def auto_assign_rank_and_suit(self):
        """
        Intended for internal class use only
        Auto assigns the variables below based on the card_num given
        card_suit - Represents the suit of the card, either Heart, Spade,
            Clover, and Diamond
        card_rank - The rank of the card, Ace, Jack, Queen, or King
        """
        # Spades suits
        if self.card_num is 0:
            self.card_rank = "Ace"
            self.card_suit = "Spades"
        elif self.card_num > 0 and self.card_num < 10:
            self.card_rank = str(self.card_num + 1)
            self.card_suit = "Spades"
        elif self.card_num is 10:
            self.card_rank = "Jack"
            self.card_suit = "Spades"
        elif self.card_num is 11:
            self.card_rank = "Queen"
            self.card_suit = "Spades"
        elif self.card_num is 12:
            self.card_rank = "King"
            self.card_suit = "Spades"

        # Hearts suits
        elif self.card_num is 13:
            self.card_rank = "Ace"
            self.card_suit = "Hearts"
        elif self.card_num > 13 and self.card_num < 23:
            self.card_rank = str(self.card_num - 12)
            self.card_suit = "Hearts"
        elif self.card_num is 23:
            self.card_rank = "Jack"
            self.card_suit = "Hearts"
        elif self.card_num is 24:
            self.card_rank = "Queen"
            self.card_suit = "Hearts"
        elif self.card_num is 25:
            self.card_rank = "King"
            self.card_suit = "Hearts"

        # Clovers suits
        elif self.card_num is 26:
            self.card_rank = "Ace"
            self.card_suit = "Clubs"
        elif self.card_num > 26 and self.card_num < 36:
            self.card_rank = str(self.card_num - 25)
            self.card_suit = "Clubs"
        elif self.card_num is 36:
            self.card_rank = "Jack"
            self.card_suit = "Clubs"
        elif self.card_num is 37:
            self.card_rank = "Queen"
            self.card_suit = "Clubs"
        elif self.card_num is 38:
            self.card_rank = "King"
            self.card_suit = "Clubs"

        # Diamonds suits
        elif self.card_num is 39:
            self.card_rank = "Ace"
            self.card_suit = "Diamonds"
        elif self.card_num > 39 and self.card_num < 49:
            self.card_rank = str(self.card_num - 38)
            self.card_suit = "Diamonds"
        elif self.card_num is 49:
            self.card_rank = "Jack"
            self.card_suit = "Diamonds"
        elif self.card_num is 50:
            self.card_rank = "Queen"
            self.card_suit = "Diamonds"
        elif self.card_num is 51:
            self.card_rank = "King"
            self.card_suit = "Diamonds"
        else:
            print("Error: card_num not a value between 0-51")

    def get_suit(self):
        """
        :return String representing the suit of the card, Spades, Clovers,
            Clubs, Hearts
        """
        return self.card_suit

    def get_rank(self):
        """
        :return String representing rank of the card, Aces, Jack, Queen,
            King, or number of the card
        """
        return self.card_rank

    def get_value(self):
        """
        :return String representing value of the card between 0 to 51
        """
        return self.card_num

    def face_down(self):
        """
        Method flips the card face-down, cards are face-down by default.
            False is equivalent to down
        """
        self.card_face = False

    def face_up(self):
        """
        Method flips hidden cards face-up, making them no longer hidden.
            True is equivalent to up
        """
        self.card_face = True

    def __str__(self):
        """
        :return String representation of the card, if the card is face-up
            returns "5 of Diamonds", if the card is face down, returns
            "<facedown>"
        """
        if self.card_face is True:
            return str(self.card_rank + " of " + self.card_suit)
        else:
            return "<facedown>"
