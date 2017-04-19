class Attack:
    #Encapsulates the concept of an attack

    def __init__(self,name,number_of_die,sides_of_die,damage_type):
        """Creates an attack with private attributes.

        Adds _name,_sides,_number, and _type
        to self, with values provided by the arguments.

        """
        self._name = name
        self._sides = sides_of_die
        self._number = number_of_die
        self._type = damage_type



    def get_attack_type(self):
        """Returns the type of attack, as a string."""
        return self._type


    def get_damage(self):
        """Returns a damage value for the attack.

        Rolls _number number of _sides sided dice, using
        DiceRoller r, and returns the resulting value."""
        return DiceRoller().roll(self._number, self._sides)

    def set_attack_name(self,attack):
        attack = name


    def get_attack_name(self):
        """Returns the name of the attack"""
        return self._name

    def set_number(self,value):
        value = number_of_die


    def get_number(self):
        return self._number


    def set_sides(self,side):
        side = sides_of_die

    def get_sides(self):
        return self._sides
