# Made by Jasque Saydyk and Alex Carpentien
# Lab 07 - Game Show
# Section 2, Mar. 25, 2017
# Description - Creates a series of methods that create a
# game show in the style of "Do you want to be a millionare"
import random
import sys
import operator
import copy

highScores = {}
questions = [
            {
                "Question": "Which insect shorted out an early computer and" +
                            " inspired the term 'computer bug'?",
                "Answers": [
                    "A: Moth",
                    "B: Roach",
                    "C: Fly",
                    "D: Japanese Beetle"],
                "Correct": "A"
            },

            {
                "Question": "Which of these U.S. Presidents appeared on the" +
                            " television series ‘Laugh-In’?",
                "Answers": [
                    "A: Lyndon Johnson",
                    "B: Richard Nixon",
                    "C: Jimmy Carter",
                    "D: Gerald Ford"],
                "Correct": "A"
            },

            {
                "Question": "In the children’s book series, where is" +
                            " Paddington Bear originally from?",
                "Answers": [
                    "A: India",
                    "B: Peru",
                    "C: Canada",
                    "D: Iceland",
                    "E: Poland"],
                "Correct": "B"
            },

            {
                "Question": "Nephelococcygia’ is the practice of doing what?",
                "Answers": [
                    "A: Finding shapes in clouds",
                    "B: Sleeping with your eyes open",
                    "C: Swimming in freezing water"],
                "Correct": "A"
            },

            {
                "Question": "Which of the following men does not have a" +
                            " chemical element named after him?",
                "Answers": [
                    "A: Albert Einstein",
                    "B: Niels Bohr",
                    "C: Issac Newton",
                    "D: Enrico Fermi",
                    "E: Nelson Mandela"],
                "Correct": "C"
            },

            {
                "Question": "Who is credited with inventing the first" +
                            " mass-produced helicopter?",
                "Answers": [
                    "A: Igor Sikorsky",
                    "B: Elmer Sperry",
                    "C: Ferdinand von Zeppelin",
                    "D: Gottlieb Daimler"],
                "Correct": "A"
            },

            {
                "Question": "What letter must appear at the beginning of the" +
                            " registration number of any non-military " +
                            " aircraft in the U.S?",
                "Answers": [
                    "A: N",
                    "B: A",
                    "C: U",
                    "D: L",
                    "E: Z"],
                "Correct": "A"
            },

            {
                "Question": "Who did artist Grant Wood use as the model" +
                            " for the farmer in his classic painting" +
                            " American Gothic?",
                "Answers": [
                    "A: Traveling salesman",
                    "B: Local sheriff",
                    "C: His dentist",
                    "D: His butcher"],
                "Correct": "C"
            },

            {
                "Question": "The U.S. icon 'Uncle Sam' was based on Samuel" +
                            " Wilson, who worked during the War of 1812 as" +
                            " a what?",
                "Answers": [
                    "A: Meat inspector",
                    "B: Mail deliverer",
                    "C: Historian",
                    "D: Weapons Mechanic"],
                "Correct": "A"
            },

            {
                "Question": "Which of the following landlocked countries" +
                            " is entirely contained within another country?",
                "Answers": [
                    "A: Lesotho",
                    "B: Burkina Faso",
                    "C: Mongolia",
                    "D: Luxembourg",
                    "E: Afghanistan"],
                "Correct": "A"
            }
            ]


def resetCopyQuestions():
    """
    Makes a copy of the questions for use by the program
    """
    copyQuestions = copy.deepcopy(questions)
    return copyQuestions


def mainMenu():
    """
    Creates the Main menu, and runs the function responsible for
    each section, asks for user input in the method
    """
    # Print game title
    print("\nBecome a Real (Fake) Millionare!!!!!!!!")

    # Ask for user input
    while True:
        try:
            menu = int(input(
                     "Enter the number to access"
                     "1: To play the game\n" +
                     "2: To view the High score table\n" +
                     "3: To view the game's credits\n" +
                     "4: To quit the game\n" +
                     "Input: "))
            if menu < 1 or menu > 4:
                print("Enter input again\n")
            else:
                break
        except ValueError:
            print("Input number, try again\n")

    return menu


def askQuestion(copyQuestions):
    """
    Asks questions until wrong and determines if the answer the user inputted
    is correct or not. If the user inputs the question correctly, it removes
    the question from the list. If user gets question wrong, implement quit
    function
    """
    random.shuffle(copyQuestions)
    singleQuestion = copyQuestions[0]
    print("-----------------------")

    while True:
        # Print question and possible answers
        print(singleQuestion["Question"])
        print(singleQuestion["Answers"])

        # Ask for user input, wrapped in while loop to determine
        # if answer is correct or inputted correctly
        userAnswer = input("Enter letter of the answer you choose: ")
        askedQuestion = True

        # Check if the answer is valid, being a length of one
        if len(userAnswer) == 1:
            # If user is correct
            userAnswer = userAnswer.upper()
            if userAnswer == singleQuestion["Correct"]:
                print("Correct\n")
                # Remove the question from the list
                del copyQuestions[0]
                return copyQuestions
            else:
                print("Wrong\n")
                return False
        # If user is wrong
        else:
            print("\nWrong input, try putting in one character")


def credits():
    """
    Prints the credits
    """
    print("-------------------------")
    print("\nThis game was created by Jasque Saydyk and Alex Carpentieri")


def inputHighScore(correct):
    """
    Asks user if they want to input a high score,
    """
    # Ask if user wants to input high score
    loopbreak = False
    while loopbreak is False:
        inputHighScore = input("Do you want to enter high score?:(Y/N)")
        if(inputHighScore.upper() == "Y"):
            # If yes, then ask for name
            name = input("Name for high score: ")
            # Store into list(as a dictionary in list)
            highScores[name] = correct
            break
        # Quit method
        elif(inputHighScore.upper() == "N"):
            break
        else:
            print("Incorrect input, try again")


def printHighScoreTable():
    """
    Outputs a table listing the recorded high scores in decsending order
    """
    # Prints everything in high score list
    print("--------------------")
    print("\nCurrent High Scores")
    sortedHighScores = sorted(highScores.items(),
                              key=operator.itemgetter(1),
                              reverse=True)
    for x in sortedHighScores:
        print(str(x[0]) + "  Score = " + str(x[1]))


def quit():
    """
    Ends the program
    """
    print("\nThanks for playing")
    sys.exit()


def main():
    """
    The main loop of the program that runs everything
    """
    currentCorrect = 0
    newGame = True
    wrong = False

    # Do main menu
    programState = mainMenu()
    while True:
        # If tree for the various options, determined by int
        # Play the game
        if programState == 1:
            # reset list if new game
            if newGame is True:
                copyQuestions = resetCopyQuestions()
                currentCorrect = 0
                newGame = False
                wrong = False
            # If there is no questions left, you win
            if len(copyQuestions) == 0:
                print("\nCongratulations, all questions correct")
                print("You get a million funny money!!!!\n")
                inputHighScore(currentCorrect)
                printHighScoreTable()
                newGame = True
                programState = mainMenu()
            # If you answer a question incorrectly
            elif wrong is True:
                inputHighScore(currentCorrect)
                printHighScoreTable()
                newGame = True
                programState = mainMenu()
            else:
                result = askQuestion(copyQuestions)
                # Determine if question is correct
                if result is False:
                    wrong = True
                else:
                    copyQuestions = result
                    currentCorrect += 1

        # View the High Score Table
        elif programState == 2:
            printHighScoreTable()
            programState = mainMenu()
        # View the game's credits
        elif programState == 3:
            credits()
            print()
            programState = mainMenu()
        # Quit the game
        elif programState == 4:
            quit()

# Run main
if __name__ == "__main__":
    main()
