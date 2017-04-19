import random


class DiceRoller:
    #A utility class for dice rolling

    def roll(self,times,sides):
        # Rolls times number of sides-sided dice; returns the total
        total = 0
        for i in range(times):
            roll = random.randint(1,sides)
            total += roll
        return total
