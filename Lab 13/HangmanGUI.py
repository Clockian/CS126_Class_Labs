# Made by Jasque Saydyk
# Lab 13 - Hangman
# Section 2, May 8, 2017
# Description - Creates the window and drawings for Hangman
import turtle


class HangmanGUI:

    def __init__(self, background, word):
        """
        Problably setup window, window title, and call on other methods to draw
        other stuff, like the gallows and number of blanks
        """
        turtle.speed(100)
        turtle.pencolor("#00aaff")

        self.setupWindow(background)
        self.drawGallows()
        self.updateWord(word)

    def setupWindow(self, background):
        """
        Sets up the window used to display the program
        """
        screen = turtle.Screen()
        screen.setup(1024, 682)
        screen.bgpic(background)

        turtle.penup()
        turtle.sety(260)
        turtle.write("HANGMAN", align="center", font=("Arial", 40, "bold"))

        turtle.setposition(-500, 0)
        turtle.write("Guess the word: ", font=("Arial", 20, "bold"))

        turtle.setposition(-250, 220)
        turtle.write("Used Letters", font=("Arial", 20, "bold"))

        turtle.home

    def drawGallows(self):
        """
        Draws the Gallows on screen for Hangman
        """
        turtle.setposition(100, 150)
        turtle.pendown()
        turtle.pen(pensize=10)

        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(300)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.right(90)
        turtle.forward(100)

        turtle.pen(pensize=1)
        turtle.penup()
        turtle.home()

    def updateWord(self, word):
        """
        Updates current progress on word on screen
        """
        turtle.setposition(-280, 0)
        turtle.write(word, font=("Consolas", 20, "bold"))

        turtle.home()

    def takeInput(self):
        """
        Handles taking the input of the game from the window
        """
        return turtle.textinput("Letter Guess", "Type letter guess:")

    def updateIncorrectLetters(self, word):
        """
        Updates the incorrect letters used on screen
        """
        turtle.setposition(-250, 180)
        turtle.write(word, font=("Arial", 20, "bold"))

        turtle.home()

    def victoryScreen(self, word):
        """
        Displays the victory screen and obtains input from the player
        as to whether to continue or end
        """
        turtle.setposition(0, -300)
        turtle.write("YOU WON!!!! Word was: " + word, align="center",
                     font=("Arial", 40, "bold"))
        answer = turtle.textinput("Play Again",
                                  "Type Y/N if you want to play again:")
        if answer.upper() == "Y":
            return True
        else:
            return False

    def loseScreen(self, word):
        """
        Displays the lose screen and obtains input from the player
        as to whether to continue or end
        """
        turtle.setposition(0, -300)
        turtle.write("YOU LOSE!!!! Word was: " + word, align="center",
                     font=("Arial", 40, "bold"))
        answer = turtle.textinput("Play Again",
                                  "Type Y/N if you want to play again:")
        if answer.upper() == "Y":
            return True
        else:
            return False

    def newGame(self, background, word):
        """
        Setups a new game by clearing the screen and reseting up all
        the drawings
        """
        turtle.clearscreen()
        turtle.speed(100)
        turtle.pencolor("#00aaff")
        self.setupWindow(background)
        self.drawGallows()
        self.updateWord(word)

    def endGame(self):
        """
        Terminates the window when game is done
        """
        turtle.bye()

    def drawHead(self):
        """
        Draws the head of the hanged man on screen
        """
        turtle.setposition(100, 100)
        turtle.pendown()
        turtle.pen(pensize=3)

        turtle.circle(25)

        turtle.pen(pensize=1)
        turtle.penup()
        turtle.home()

    def drawBody(self):
        """
        Draws the body of the hanged man on screen
        """
        turtle.setposition(100, 100)
        turtle.pendown()
        turtle.pen(pensize=3)

        turtle.right(90)
        turtle.forward(75)

        turtle.pen(pensize=1)
        turtle.penup()
        turtle.home()

    def drawLeftArm(self):
        """
        Draws the left arm of the hanged man on screen
        """
        turtle.setposition(100, 90)
        turtle.pendown()
        turtle.pen(pensize=3)

        turtle.right(135)
        turtle.forward(50)

        turtle.pen(pensize=1)
        turtle.penup()
        turtle.home()

    def drawRightArm(self):
        """
        Draws the right arm of the hanged man on screen
        """
        turtle.setposition(100, 90)
        turtle.pendown()
        turtle.pen(pensize=3)

        turtle.right(45)
        turtle.forward(50)

        turtle.pen(pensize=1)
        turtle.penup()
        turtle.home()

    def drawLeftLeg(self):
        """
        Draws the left leg of the hanged man on screen
        """
        turtle.setposition(100, 25)
        turtle.pendown()
        turtle.pen(pensize=3)

        turtle.right(135)
        turtle.forward(50)

        turtle.pen(pensize=1)
        turtle.penup()
        turtle.home()

    def drawRightLeg(self):
        """
        Draws the right leg of the hanged man on screen
        """
        turtle.setposition(100, 25)
        turtle.pendown()
        turtle.pen(pensize=3)

        turtle.right(45)
        turtle.forward(50)

        turtle.pen(pensize=1)
        turtle.penup()
        turtle.home()
