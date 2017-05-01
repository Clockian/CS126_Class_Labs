# Made by Jasque Saydyk and Ian Otto
# Lab 12 - Blackjack
# Section 2, May 1, 2017
# Description - Represents a basic bank


class ChipBank:

    def __init__(self, value):
        """
        :param value - Numeric value to start the ChipBank balance at
        """
        self.value = value
        self._log_file = None

    def withdraw(self, amount):
        """
        :param amount - Numeric amount to withdraw
        :return Numeric value actually withdrawn, if bank is less than amount,
            returns all of the money possible
        """
        pBalance = self.value
        if pBalance - amount <= 0:
            self.value = 0
            self.record_change(-amount)
            return pBalance
        else:
            self.value -= amount
            self.record_change(-amount)
            return amount

    def deposit(self, amount):
        """
        :param amount - Numeric amount to deposit
        """
        self.value += amount
        self.record_change(amount)

    def get_balance(self):
        """
        :return Numeric balance currently held in ChipBank
        """
        return self.value

    def record_change(self, amount):
        """
        :param amount - Number to be log as the transaction
        """
        if self._log_file is None:
            pass
        else:
            self._log_file.write(str(self.value) + " " + str(amount) + "\n")

    def record(self, handle):
        """
        This function logs deposits and withdraws to an external file
        :param handle - File handle to write to a file
        """
        self._log_file = handle

    def __str__(self):
        """
        :return String describing the different chips held along with the total
            balance. Black chips - 100, Green chips - 25, Red chips - 5, Blue
            chips - 1. Ex: " 1 blacks, 2 greens - totaling $150"
        """
        temp_val = self.value

        blacks = temp_val // 100
        temp_val -= blacks * 100

        greens = temp_val // 25
        temp_val -= greens * 25

        reds = temp_val // 5
        temp_val -= reds * 5

        blues = temp_val

        return "%d blacks, %d greens, %d reds, %d blues, totaling $%d" %\
               (blacks, greens, reds, blues, self.value)
