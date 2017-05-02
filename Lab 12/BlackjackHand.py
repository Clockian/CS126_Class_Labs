# Made by Jasque Saydyk and Ian Otto
# Lab 12 - Blackjack
# Section 2, May 1, 2017
# Description - Represents a hand of Blackjack


class BlackjackHand:

    def __init__(self):
        """
        Sets up list for storing cards
        """
        self._dealt = []

    def add_card(self, new_card):
        """
        Adds a card to the hand.
        :param new_card - The Card object to be added to the hand
        """
        self._dealt.append(new_card)

    def get_value(self):
        """
        Returns a numeric point value of the current hand. This should be the
        sum of the point values of each card. In our implementation of
        blackjack, an Ace should be either 11 points, or 1, to give the player
        the highest score without exceeding 21. Hint: First count the total
        points assuming all aces are 11, along with the number of aces, then
        decrement point total as the rules allow.
        :return A numeric value representing the value of the hand.
        """
        total = 0
        for i in self._dealt:
            total += i.get_value()

        if total > 21:
            for i in self._dealt:
                if i.get_value() == 11:
                    total -= 10
                    if total < 22:
                        break
        return total

    def clear_hand(self):
        """
        Removes all cards from the hand
        """
        self._dealt = []

    def face_up_all(self):
        """
        Flips all current cards in hand to face-up
        """
        for i in self._dealt:
            i.face_up()

    def face_up_dealer_initial(self):
        """
        Turn up the first dealt of the dealer's cards
        """
        self._dealt[0].face_up()

    def __str__(self):
        """
        Returns a string representation of the current hand. The resulting
        string should contain the __str__() value of each card, delimited by
        commas
        :return A string representing all the cards in the hand
        """
        built_str = ""
        for i, v in enumerate(self._dealt):
            if i != 0:
                built_str += ", "
            built_str += str(v)
        return built_str
