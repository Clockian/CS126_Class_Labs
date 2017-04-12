class ChipBank:

    
    def __init__(self, value):
        """
        :param value - Numeric value to start the ChipBank balance at
        """
        self.value = value


    def withdraw(self, amount):
        """
        :param amount - Numeric amount to withdraw
        :return Numeric value actually withdrawn, if bank is less than amount,
            returns all of the money possible
        """
        if amount >= self.value:
            withdrawn = self.value
            self.value = 0
            return withdrawn
        else:
            self.value -= amount
            return amount

    def deposit(self, amount):
        """
        :param amount - Numeric amount to deposit
        """
        self.value += amount


    def get_balance():
        """
        return Numeric balance currently helf in ChipBank
        """
        return self.value


    def record(handle):
        """
        This function logs deposits and withdraws to a 
        :param handle - File handle to write to a file
        """


    def __str__():
        """
        :return String describing the different chips held along with the total
            balance. Black chips - 100, Green chips - 25, Red chips - 5, Blue
            chips - 1. Ex: " 1 blacks, 2 greens - totaling $150"
        """
        amount = self.value

        black_num = self.value % 100
        amount -= black_num * 100

        green_num = self.value % 25
        amount -= green_num * 25

        red_num = self.value % 5
        amount -= red_num * 5

        return str(black_num + " blacks, " + green_num + " greens, " + red_num +
                   " reds, " + amount + " blues - totaling $" + self.value)
