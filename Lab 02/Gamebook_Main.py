# Made by Jasque Saydyk and Isai Martinez
# Lab 02 - Gamebook
# Section 2, Feb. 2, 2017
# Description - This is a simple choose-your-own-adventure story.
# The user types in the branch to explore until they get victory or death
# The program continues until the player quits when they die
# The program inform the player of any errors they input and doesn't crash

# Data
paragraph1 = ("\nYou awaken from your bed, feeling strange." +
              "\nSomething is going to happen today, something" +
              "\nbig, but you don’t know what….")
paragraph2 = ("\nFeeling tired, you go to get a couple more moments of sleep" +
              "\nAs you cuddle up, you feel the bed is warm…. And moist…." +
              "\nAs you look up, you realize in horror that you are eaten " +
              "\nby a Bedoster")
paragraph3 = ("\nYou get up, the carpet tickles your feet." +
              "\nYou then fall to the ground laughing at how much the" +
              "\ncarpet tickles you. You realize you cannot breath in" +
              "\nYou die, with a smile on you face on the carpet.")
paragraph4 = ("\nYou sit up, stretch and let out an uplifting yawn that " +
              "dispels the sleep from your body.\nYou get out of bed," +
              "putting on your normal clothes, then approach the stairs" +
              "\nBy the stairs, you see an old family chest you haven’t " +
              "opened in years…")
paragraph5 = ("\nYou sense an eerie presence pouring from the chest" +
              "\nAs you approach it, it strangely seems to move and " +
              "shift, despite being rigid" +
              "You place both of your hands on the chest....")
paragraph6 = ("\nYou descend the stairs, feeling relieved the more you move." +
              "\nWhen you get to the bottom, you think that everything is " +
              "going to be all right." +
              "You leave the house, confident for a new day!" +
              "\nThanks for playing\nGame Over")
paragraph7 = ("\nThe chest is freezing, you move to remove your hands, " +
              "but they are stuck in place." +
              "\nThe lid opens, and the skin of the chest crawls into " +
              "the void, dragging you along." +
              "\nYou struggle in vain, and as the darkness surrounds you " +
              "and the light from the lid grows fainter, you relax into " +
              "sleep once again")
paragraph8 = ("\nThe chest feels cool... and fleshy..." +
              "\nSuddenly, arms unfold from the chest and grabbing your " +
              "body, it's long fingers coiling around you like rope." +
              "\nThe chest opens, revealing teeth, a disgusting tongue, and " +
              "infinite darkness.")
paragraph9 = ("\nYour hands are burning, flesh melting as you are unable " +
              "to remove them"
              "\nYou realize, to late, the difference between Fahrenheit " +
              "and Celsius."
              "\nYou blackout due to shock, as your body is pulled to the " +
              "chest, burning into nothing.")

# This function runs until the user gives a valid YES or NO to the question
# Try Again? If yes, main program will use breaks to get back to the beginning
# of the main loop, else main program will set end to true and end program


def quitChoice():
    while(True):
        choice = input("\nTry Again? YES/NO: ")
        choice = choice.upper()
        if(choice == "NO"):
            return True
        elif(choice == "YES"):
            return False
        else:
            print("\nERROR: Enter one of the all-cap words")

# Quits the game when True
end = False

# Main loop of the game, continues until player explicitly quits
while(end is False):
    print(paragraph1)
    choice = input("Do you STAY, GET UP, or YAWN? ")  # Input for first choice
    choice = choice.upper()  # Changes the input to all uppercase

    # CHOICE 1-1 #
    if(choice == "STAY"):
        print(paragraph2)
        if(quitChoice() is True):
            end = True

    # CHOICE 1-2 #
    elif(choice == "GET UP"):
        print(paragraph3)
        if(quitChoice() is True):
            end = True

    # CHOICE 1-3 #
    elif(choice == "YAWN"):
        while(end is False):
            print(paragraph4)
            choice = input("Do you DESCEND or INVESTIGATE? ")
            choice = choice.upper()  # Changes the input to all uppercase

            # CHOICE 2-1 #
            if(choice == "DESCEND"):
                print(paragraph6)
                end = True  # Victory, automatically end game

            # CHOICE 2-2 #
            elif(choice == "INVESTIGATE"):
                while(end is False):
                    print(paragraph5)

                    choice = input("How hot does the chest feel? ")

                    # Try-Exception block to catch errors
                    # on the int cast and the TypeError
                    try:
                        # Convert String of number to int
                        choice = int(choice)

                        # CHOICE 3-1 #
                        if(choice < 30):
                            print(paragraph7)
                            if(quitChoice() is True):
                                end = True
                            break

                        # CHOICE 3-2 #
                        elif(choice >= 30 and choice <= 60):
                            print(paragraph8)
                            if(quitChoice() is True):
                                end = True
                            break

                        # CHOICE 3-3 #
                        elif(choice > 60):
                            print(paragraph9)
                            if(quitChoice() is True):
                                end = True
                            break

                        else:
                            print("\nError: Enter an integer")

                    # Catch block for errors in Try block
                    except ValueError:
                        print("\nERROR: Enter a number, not a string")
                    except TypeError:
                        print("\nERROR: TypeError, this shouldn't happen")

                break  # Choice 2, Try again, to get to main loop

            else:
                print("\nERROR: Enter one of the all-cap words")
    else:
        print("\nERROR: Enter one of the all-cap words")
