# Made by Jasque Saydyk and Miguel Quinones
# Lab 11 - RPG
# Section 2, April 19, 2017
# Description - Represents an dice rolling class
# A utility class for dice rolling
import random


class DiceRoller:

    def roll(self, times, sides):
        """
        Rolls times number of sides-sided dice; returns the total
        """
        total = 0
        for i in range(times):
            roll = random.randint(1, sides)
            total += roll
        return total
