# Made by Jasque Saydyk and Miguel Quinones
# Lab 11 - RPG
# Section 2, April 19, 2017
# Description - Represents an Adventurer class that Wizard and Fighter inherit,
# Encapsulates the concept of an adventurer.
import random


class Adventurer:

    def __init__(self, name, hit_points, defense, magic_defense, initiative):
        """
        Creates an adventurer with private attributes.
        Adds _name,_hit_points,_defense,_magic_defense, and _initiative to
        self, with values provided by the arguments.
        """
        self._name = name
        self._HP = hit_points
        self._defense = defense
        self._MD = magic_defense
        self._initiative = initiative

    def is_alive(self):
        """
        Returns True if this object has more than 0 hit points.
        """
        if self._HP > 0:
            return True
        else:
            return False

    def roll_initiative(self):
        """
        Returns a random integer between 0 and this object's _initiative value.
        """
        return random.randint(0, self._initiative)

    def take_damage(self, amount, damage_type):
        """
        Applies damage to this object's attributes.

        If the damage type is "physical", reduce this object's hit points by
        what is left after reducing amount by the object's defense. If the
        damage type is "magic", reduce the object's hit points by what is left
        after reducing amount by the object's magic_defense. (For instance,
        let's say an Adventurer with 10 defense takes 18 as the amount ofdamage
        and "physical" as the damage_type. We would subtract the defense from
        the amount, so that the Adventurer really only takes 8 damage. Then, we
        subtract 8 from the adventurer's hit points. An Adventurer's defense
        and magic defense never decrease.)

        Of course, make sure that the damage applied can never be less than 0
        (so if an adventurer with 4 defense takes 3 physical damage, theyreally
        take 0 damage overall, not -1), and that an adventurer can never have
        negative hit points (so if an adventurer with 3 hit points remaining
        takes 5 damage, they now have 0 hit points, not -2).

        Also prints out information about the damage application process,
        something like 'Gandalf suffers 1 damage after 4 defense and has 12 hit
        points left.'
        """
        if(damage_type == "physical"):
            applied_damage = amount - self._defense
            if(applied_damage < 0):
                applied_damage = 0
            self._HP -= applied_damage
            print(str(self._name) + " suffers " + str(applied_damage) +
                  " damage after " + str(self._defense) + " defense and has " +
                  str(self._HP) + " hit points left.")

        if (damage_type == "magic"):
            applied_damage = amount - self._MD
            if (applied_damage < 0):
                applied_damage = 0
            self._HP -= applied_damage
            print(str(self._name) + " suffers " + str(applied_damage) +
                  " damage after " + str(self._MD) + " defense and has " +
                  str(self._HP) + " hit points left.")

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_HP(self, HP):
        self._HP = HP

    def get_HP(self):
        return self._HP

    def set_defense(self, defense):
        self._defense = defense

    def get_defense(self):
        return self._defense

    def set_magic_defense(self, MD):
        self._MD = MD

    def get_magic_defense(self):
        return self._MD

    def set_initiative(self, initiative):
        self._initiative = initiative

    def get_initiative(self):
        return self._initiative
