# Made by Jasque Saydyk and Miguel Quinones
# Lab 11 - RPG
# Section 2, April 19, 2017
# Description - Represents a Fighter


class Fighter(Adventurer):
    """
    Encapsulates a Fighter class, inheriting from Adventurer.

    Fighters are defined by 40 health point ( HP), defense of 10 ( DEF),
    and magic defense ( MAG DEF) of 4, which are stored as class variables.

    Note: It is convention to capitalize the names of variables that are to
    remain constant, and note the use of an underscore to indicate
    that the variables are private.
    """
    _HP = 40
    _DEF = 10
    _MAG_DEF = 4

    def __init__(self, name, initiative):
        """
        Creates a Fighter object.

        Calls the superclass init method with name, HP, DEF,
        MAG DEF, and initiative.

        Also adds a variable melee that references an instance of the
        Attack class. For our simple game, this lets us create fixed
        attacks such as Attack(”Slash”, 1, 8, ”physical”).
        """
        super().__init__(name, Fighter._HP, Fighter._DEF, Fighter._MAG_DEF,
                         initiative)
        self._melee = Attack(”Slash”, 1, 8, ”physical”)

    def strike(self):
        """
        Calculates and returns information about a physical strike from
        this object.

        Returns a tuple, consisting of the damage value and the damage type.
        The damage value is obtained by calling the get damage() method on
        melee, while the type is obtained by calling get attack type() on
        melee.

        Also prints out information about the strike, something like
        ’Aragorn attacks with Slash for 5 physical damage.’
        """
        damage = melee.getDamage()
        attack_type = melee.get_attack_type()

        print(str(self.get_name()) + " attacks with " + str(attack_type) +
              " for " + str(melee.get_name()) + str(damage) + " damage.")

        return (damage, attack_type)

    def __str__(self):
        """
        Returns a string representation of this object, something like
        ’Aragorn with 40 hit points and a Slash attack (1d8).’ The abbreviation
        in the parentheses represents the number and type of dice used for the
        attack, so 1d8 means 1 die with 8 sides is rolled.
        """
        s = (str(self.get_name()) + " with " + str(self._HP) +
             " hit points and a " + str(melee.get_name()) + " attack (" +
             str(melee.get_number_of_die) + "d" + str(melee.get_sides_of_die))
        return s
