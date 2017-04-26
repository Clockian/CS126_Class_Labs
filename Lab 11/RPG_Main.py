# Made by Jasque Saydyk and Miguel Quinones
# Lab 11 - RPG
# Section 2, April 19, 2017
# Description - Main class for running and testing code
from Adventurer import *
from Fighter import *
from Wizard import *

if __name__ == "__main__":
    # Create a Fighter object by providing a name and
    # initiative value to the Fighter constructor, and print the object out
    a = Fighter("Aragorn", 20)
    print("Created: ", a)

    # Create a Wizard object, using the Wizard constructor with similar
    # information as that provided for Fighter, and print the object out
    b = Wizard("Gandalf", 20)
    print("Created: ", b)

    # Create a variable to keep track of the rounds of combat
    num_rounds = 1

    # As long as both combatants are alive, keep fighting rounds
    while(a.is_alive() is True and b.is_alive() is True):
        # Roll initiative for both combatants; whichever one has the highest
        # initiative gets to attack this round. The other one... sits there
        # If the initiative values are equal, roll them again until one is
        # higher.
        #
        # An attack works by getting a damage value and type by using the
        # cast() or strike()method from whatever object won initiative. Then,
        # call take damage() on thelosing object using the values that
        # cast()/strike() returned
        print()
        print("** ROUND " + str(num_rounds))
        if(a.roll_initiative() > b.roll_initiative()):
            print(a.get_name() + " wins initiative!")
            damage = a.strike()
            b.take_damage(damage[0], damage[1])

            # Victory message
            if(b.is_alive() is False):
                print()
                print(str(a.get_name()) + " has won with " + str(a.get_HP()) +
                      " hit points left!")
        else:
            print(b.get_name() + " wins initiative!")
            damage = b.cast()
            a.take_damage(damage[0], damage[1])

            # Print out a message indicating which combatant is still alive
            # and their remaining hit points
            if(a.is_alive() is False):
                print()
                print(str(b.get_name()) + " has won with " + str(b.get_HP()) +
                      " hit points left!")

        # Don’t forget to increment your round counter
        num_rounds += 1
