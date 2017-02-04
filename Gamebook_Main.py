# Made by Jasque Saydyk and Isai Martinez
# Lab 02 - Gamebook
# Section 2, Feb. 2, 2017
# Description - This is a simple choose-your-own-adventure story.
# The user types in the branch to explore until they get victory or death
# The program continues until the player quits when they die
# The program inform the player of any errors they input and doesn't crash

# Quits the game when True
end = False

# Main loop of the game, continues until player explicitly quits
while(end is False):
    # Paragraph 1
    print("\nYou awaken from your bed, feeling strange.")
    print("Something is going to happen today, something")
    print("big, but you don’t know what….")

    # Input for first choice
    choice = input("Do you STAY, GET UP, or YAWN? ")

    # Changes the input to all uppercase
    choice = choice.upper()

    ##############
    # CHOICE 1-1 #
    ##############
    if(choice == "STAY"):
        # Paragraph 2
        print("\nFeeling tired, you go to get a couple more moments of sleep")
        print("As you cuddle up, you feel the bed is warm…. And moist….")
        print("As you look up, you realize in horror that you are eaten " +
              "by a Bedoster")

        # Quit Choice Block
        while(end is False):
            choice = input("Try Again? YES/NO: ")
            choice = choice.upper()
            if(choice == "NO"):
                end = True
            elif(choice == "YES"):
                break
            else:
                print("\nERROR: Enter one of the all-cap words")

    ##############
    # CHOICE 1-2 #
    ##############
    elif(choice == "GET UP"):
        # Paragraph 3
        print("\nYou get up, the carpet tickles your feet. You then " +
              "fall to the ground laughing at how much the")
        print("Carpet tickles you. As you laugh, you realize " +
              "you cannot breath in")
        print("You die, with a smile on you face on the carpet")

        # Quit Choice Block
        while(end is False):
            choice = input("Try Again? YES/NO: ")
            choice = choice.upper()
            if(choice == "NO"):
                end = True
            elif(choice == "YES"):
                break
            else:
                print("\nERROR: Enter one of the all-cap words")

    ##############
    # CHOICE 1-3 #
    ##############
    elif(choice == "YAWN"):
        # Paragraph 4
        print("\nYou sit up, stretch and let out an uplifting " +
              "yawn that dispels the sleep from your body")
        print("You get out of bed, putting on your normal " +
              "clothes, then approach the stairs")
        print("By the stairs, you see an old family chest " +
              "you haven’t opened in years…")

        while(end is False):

            # Input for second choice
            choice = input("Do you DESCEND or INVESTIGATE? ")

            # Changes the input to all uppercase
            choice = choice.upper()

            ##############
            # CHOICE 2-1 #
            ##############
            if(choice == "DESCEND"):
                # Paragraph 6
                print("\nYou descend the stairs, feeling " +
                      "relieved the more you move.")
                print("When you get to the bottom, you " +
                      "think that everything is going to be all right.")
                print("You leave the house, confident for a new day!")
                print("\nThanks for playing \nGame Over")

                # Victory, automatically end game
                end = True

            ##############
            # CHOICE 2-2 #
            ##############
            elif(choice == "INVESTIGATE"):
                while(end is False):
                    # Paragraph 5
                    print("\nYou sense an eerie presence " +
                          "pouring from the chest")
                    print("As you approach it, it strangely " +
                          "seems to move and shift, despite being rigid")
                    print("You place both of your hands on the chest....")

                    # Input for third choice
                    choice = input("How hot does the chest feel? ")

                    # Try-Exception block to catch errors
                    # on the int cast and the TypeError
                    try:
                        # Convert String of number to int
                        choice = int(choice)

                        ##############
                        # CHOICE 3-1 #
                        ##############
                        if(choice < 30):
                            # Paragraph 7
                            print("\nThe chest is freezing, you move " +
                                  "to remove your hands, but they are stuck " +
                                  "in place.")
                            print("The lid opens, and the skin of the " +
                                  "chest crawls into the void, dragging " +
                                  "you along.")
                            print("You struggle in vain, and as the " +
                                  "darkness surrounds you and the light " +
                                  "from the lid grows fainter, you relax " +
                                  "into sleep once again")

                            # Quit Choice Block
                            while(end is False):
                                choice = input("Try Again? YES/NO: ")
                                choice = choice.upper()
                                if(choice == "NO"):
                                    end = True
                                elif(choice == "YES"):
                                    break
                                else:
                                    print("\nERROR: Enter one of the " +
                                          "all-cap words")

                            # Extra break to jump back to main loop
                            break

                        ##############
                        # CHOICE 3-2 #
                        ##############
                        elif(choice >= 30 and choice <= 60):
                            # Paragraph 8
                            print("\nThe chest feels cool... and fleshy...")
                            print("Suddenly, arms unfold from the chest and " +
                                  "grabbing your body, it's long fingers " +
                                  "coiling around you like rope.")
                            print("The chest opens, revealing teeth, a " +
                                  "disgusting tongue, and infinite darkness.")

                            # Quit Choice Block
                            while(end is False):
                                choice = input("Try Again? YES/NO: ")
                                choice = choice.upper()
                                if(choice == "NO"):
                                    end = True
                                elif(choice == "YES"):
                                    break
                                else:
                                    print("\nERROR: Enter one of the " +
                                          "all-cap words")
                            # Extra break to jump back to main loop
                            break

                        ##############
                        # CHOICE 3-3 #
                        ##############
                        elif(choice > 60):
                            # Paragraph 9
                            print("\nYour hands are burning, flesh melting " +
                                  "as you are unable to remove them")
                            print("You realize, to late, the difference " +
                                  "between Fahrenheit and Celsius.")
                            print("You blackout due to shock, as your body " +
                                  "is pulled to the chest, burning into " +
                                  "nothing.")

                            # Quit Choice Block
                            while(end is False):
                                choice = input("Try Again? YES/NO: ")
                                choice = choice.upper()
                                if(choice == "NO"):
                                    end = True
                                elif(choice == "YES"):
                                    break
                                else:
                                    print("\nERROR: Enter one of " +
                                          "the all-cap words")
                            # Extra break to jump back to main loop
                            break

                        else:
                            print("\nError: Enter an integer")

                    # Catch block for errors in Try block
                    except ValueError:
                        print("ERROR: Enter a number, not a string")
                    except TypeError:
                        print("ERROR: TypeError")

                # Extra break for Quit Choice Block to get to main loop
                break
            else:
                print("\nERROR: Enter one of the all-cap words")
    else:
        print("\nERROR: Enter one of the all-cap words")
