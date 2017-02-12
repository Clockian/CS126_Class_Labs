# Made by Jasque Saydyk and Michael Horton
# Lab 03 - MathQuiz
# Section 2, Feb. 11, 2017
# Description - This is a simple math quiz program.
# The user is asked a question, which they must type
# the answer for. The user is then shown how many they got right
# The program continues until the player quits at a given prompt

from random import randint
from random import choice

# Advance question strings
question1 = ("\nWhat is the area of a rectangle with the length %d and the\n" +
             "width of %d? ")

question2 = ("\nBilly and Mandy are arguing about how to split up candy.\n" +
             "They come to an agreement that Mandy should get two\n" +
             "candies for every candy that Bill gets. If there are\n" +
             "%d candies, how many candies should Mandy receive? ")

question3 = ("\nAlex, Fred, and John all get into a fight, and when\n" +
             "discovered by their parents, are severely reprimanded for\n" +
             "it. Alex gets %d minutes of time out and no video game\n" +
             "for a week. John gets Alex’s timeout squared. Fred get half\n" +
             "as much time out as John. How much time out does Fred get? ")

question4 = ("\nEbony and Alex both agree that the fairest way to split\n" +
             "their river pebbles to finish their fort’s artwork is\n" +
             "three pebbles for Ebony for every two pebbles Alex gets.\n" +
             "They’ve collected a combined amount of %d pebbles. How many\n" +
             "pebbles with they have left to throw back into the river? ")

question5 = ("\nThe Persians have three archers for every calvary,\n" +
             "whereas the Macedonians have three cavalry for every\n" +
             "five hoplites they have. The Persians have %d calvary,\n" +
             "whereas the Macedonians have %d Hoplites. Who has the larger\n" +
             "army?(Enter 0 for the Persians, enter 1 for the Macedonians): ")

end = False

# Main loop of the program
while(end is False):
    correct = 0
    inputsCorrect = False
    advanceChoice = False

    # Input filter to determine inputs are good before continuing
    while(inputsCorrect is False):
        try:
            # Cast the input to int
            numberOfQuestions = int(input("\nHow many question's would you " +
                                          "like to answer? "))

            # Determines if the inputted string is one that the program can use
            levelOfDifficulty = input("\nWhat difficulty do you want?" +
                                      "(Beginner, Intermediate, Advanced) ")

            # Convert input to all uppercase, so it doesn't
            # matter how the user inputs the word
            levelOfDifficulty = levelOfDifficulty.upper()

            # Valid string inputs the program can recognize
            if(levelOfDifficulty == "BEGINNER"):
                inputsCorrect = True
            elif(levelOfDifficulty == "INTERMEDIATE"):
                inputsCorrect = True
            elif(levelOfDifficulty == "ADVANCED"):
                inputsCorrect = True
            else:
                print("\nYou typed the difficulty incorrectly")

        # Handles error if int cast is given a string instead
        except ValueError:
            print("\nInput a number, not a string")

    ###################
    # BEGINNER Section
    ###################
    if(levelOfDifficulty == "BEGINNER"):
        # For loop for number of questions
        for i in range(numberOfQuestions):
            # Choosing random numbers for questions between 1 to 10
            n1 = randint(1, 10)
            n2 = randint(1, 10)

            # Deciding between Plus or Minus questions with coinflip
            coinFlip = choice([1, 2])
            try:
                if(coinFlip == 1):
                    questionAnswer = n1 + n2
                    userAnswer = int(input("\nWhat's %d + %d? " % (n1, n2)))
                else:
                    questionAnswer = n1 - n2
                    userAnswer = int(input("\nWhat's %d - %d? "
                                           % (n1, n2)))

                # Deciding if user input is right
                if(userAnswer == questionAnswer):
                    print("\nThat's right ----- well done.")
                    correct = correct + 1
                else:
                    print("\nNo, I'm afraid the answer is %d."
                          % questionAnswer)

            # Handles error if int cast is given a string instead
            except ValueError:
                    print("\nError: Input int, not string")

    ######################
    # Intermidate Section
    ######################
    elif(levelOfDifficulty == "INTERMEDIATE"):
        # For loop for number of questions
        for i in range(numberOfQuestions):
            # Choosing random numbers for questions between 1 to 10
            n1 = randint(1, 25)
            n2 = randint(1, 25)

            # Deciding between +, -, Multiplication, and Division
            coinFlip = choice([1, 2, 3, 4])
            try:
                if(coinFlip == 1):
                    questionAnswer = n1 + n2
                    userAnswer = int(input("\nWhat's %d + %d? " % (n1, n2)))
                elif(coinFlip == 2):
                    questionAnswer = n1 - n2
                    userAnswer = int(input("\nWhat's %d - %d? " % (n1, n2)))
                elif(coinFlip == 3):
                    questionAnswer = n1 * n2
                    userAnswer = int(input("\nWhat's %d * %d? " % (n1, n2)))
                else:
                    questionAnswer = n1 / n2
                    userAnswer = int(input("\nWhat's %d / %d? " % (n1, n2)))

                # Deciding if user input is right
                if(userAnswer == questionAnswer):
                    print("\nThat's right ----- well done.")
                    correct = correct + 1
                else:
                    print("\nIncorrect, answer is %d." % questionAnswer)

            # Handles error if int cast is given a string instead
            except ValueError:
                print("\nError: Input int, not string")

    ###################
    # Advanced section
    ###################
    elif(levelOfDifficulty == "ADVANCED"):
        # Used for determining final output
        advanceChoice = True

        # Decides randomly between the five questions
        coinFlip = choice([1, 2, 3, 4, 5])
        try:
            if(coinFlip == 1):
                n1 = randint(1, 250)
                n2 = randint(1, 250)
                questionAnswer = n1 * n2
                userAnswer = int(input(question1 % (n1, n2)))
            elif(coinFlip == 2):
                n1 = randint(6, 500)
                questionAnswer = (2*(n1//3))
                userAnswer = int(input(question2 % (n1)))
            elif(coinFlip == 3):
                n1 = randint(2, 60)
                questionAnswer = ((n1 * n1)//2)
                userAnswer = int(input(question3 % (n1)))
            elif(coinFlip == 4):
                n1 = randint(5, 600)
                questionAnswer = n1 % 5
                userAnswer = int(input(question4 % (n1)))
            else:
                n1 = randint(5000, 40000)
                n2 = randint(8000, 30000)
                persians = (n1 * 3)
                macedonians = (3 * (n2//5))
                if(persians < macedonians):
                    # Persians with bigger army
                    questionAnswer = 0
                else:
                    # Macedonians with bigger army
                    questionAnswer = 1
                userAnswer = input(question5 % (n1, n2))

            # Deciding if answer is right
            if(userAnswer == questionAnswer):
                print("\nThat's right ----- well done.")
                correct = correct + 1
            else:
                print("\nNo, I'm afraid the answer is %d." % questionAnswer)

        # Handles error if int cast is given a string instead
        except ValueError:
            print("\nError: Input int, not string")
    else:
        print("\nERROR 1: End of difficulty if-tree, couldn't interpet input")

    # Outputting the final results, there is separate output for Advanced
    if(advanceChoice is True and correct == 1):
        print("Well done!")
    elif(advanceChoice is True and correct == 0):
        print("Please ask your math teacher for help!")
    elif(correct > (numberOfQuestions * (2/3))):
        print("\nI asked you %d questions. You go %d of them right."
              % (numberOfQuestions, correct))
        print("Well done!")
    elif(correct > (numberOfQuestions * (1/3))):
        print("\nI asked you %d questions. You go %d of them right."
              % (numberOfQuestions, correct))
        print("You need more practice")
    else:
        print("\nI asked you %d questions. You go %d of them right."
              % (numberOfQuestions, correct))
        print("Please ask your math teacher for help!")

    # Runs until you give a valid Y or N to to quitting the program
    while(end is False):
        tryAgain = input("\nTry Again?(Y/N) ")
        tryAgain = tryAgain.upper()
        if(tryAgain == "N"):
            end = True
        elif(tryAgain == "Y"):
            break
        else:
            print("\nError: Input Y for yes or N for no")
