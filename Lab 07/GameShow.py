# the beginning

questions = [
              {"question": "who played the frist Batman?",
               "answers": [
                           "George Clooney",
                           "Adam West",
                           "Louis G Wilson",
                           "Christian Bale"],
               "correct": "3"},
              {"question": "What's the answer to life," +
               "the universe and everything?" +
               "answers": [
                           "Cheese",
                           "42",
                           "Tacos",
                           "Baseball"],
               "correct": "2"}]
print("Welcome to our CS126 Trivia Game")
print("Win MILLIONS!!\n")

for question in questions:
    print(question["question"])
    for i, choice in enumerate(question["answers"]):
        print(str(i + 1) + ". " + choice)
    answer = input("Choose an answer 1-4:")
    if answer ==question["correct"]:
        print("Good job.  Confetti falls in the background.")
    else:
        print("Not correct.  The audience boos."

def mainMenu():
    """
    Creates the Main menu, and runs the function responsible for
    each section, asks for user input in the method
    """
    # Print game title
    
    # Ask for user input
    menu = int(input("1 to play the game\n" +
                 "2 to view the High score table\n" +
                 "3 to view teh game's credits\n" +
                 "4 to quit the game\n" +
                 "Input: "
                 ))
    # If tree for the various options, determined by int
    if menu == 1:
        askQuestions()
    elif menu == 2:
        inputHighScore()
    elif menu == 3:
        credits()
    else:
        return False
              
              
    # Enter 1 to play the game

    # Enter 2 to view the High score table

    # Enter 3 to view the game's credits

    # Enter 4 to quit the game, return false instead


def askQuestions():
    """
    Asks questions until wrong and determines if the answer the user inputted
    is correct or not. If the user inputs the question correctly, it removes
    the question from the list. If user gets question wrong, implement quit function
    """
    #wrap in while loop
    while askQuestion == True
        # Print question and possible answers

        # Ask for user input, wrap in while loop to determine if answer is correct

        # If user is correct

            # Remove the question from the list

            # double player's current points

            # Maybe return... boolean?

        # If user is wrong

            # break loop?


def credits():
    """
    Prints the credits
    """
    # Print statements for the credits of the game
    print("This game was created by Jasque Saydyk and Alex Carpentieri\n" +
          ""
          )


def inputHighScore():
    """
    Asks user if they want to input a high score,
    """
    # ask if user wants to input high score

        # If yes, then ask for name

        # Store into list(as a dictionary in list)

    # Else, no else i think


def printHighScoreTable():
    """
    outputs a table listing the recorded high scores
    """
    # a for loop that prints everything in high score list


def quit():
    """
    Is this nessary?
    """
    # idk


def main():
    """
    The main loop of the program that runs everything
    """
    # while loop

        # do main menu

        
