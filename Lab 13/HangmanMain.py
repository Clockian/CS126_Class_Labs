# Made by Jasque Saydyk
# Lab 13 - Hangman
# Section 2, May 8, 2017
# Description - Main game loop the game exists in
from Hangman import *
from HangmanGUI import *


if __name__ == "__main__":
    filehandle = open("corncob_lowercase.txt", "r")
    game = Hangman(filehandle)
    filehandle.close()
    gui = HangmanGUI("background.png", game.getCurrentWord())

    while(True):
        letter = gui.takeInput()

        # Takes input and adds it to game
        try:
            choice = game.inputLetter(letter)

            usedLetters = game.getUsedLetters()

            gui.updateIncorrectLetters("".join(usedLetters))

            if choice is True:
                gui.updateWord(game.getCurrentWord())
        except ValueError:
            print("Error, try again")

        # Draw Hangman as more mistakes are made
        if game.getBadChoices() is 1:
            gui.drawHead()
        elif game.getBadChoices() is 2:
            gui.drawBody()
        elif game.getBadChoices() is 3:
            gui.drawLeftArm()
        elif game.getBadChoices() is 4:
            gui.drawRightArm()
        elif game.getBadChoices() is 5:
            gui.drawRightLeg()
        elif game.getBadChoices() is 6:
            gui.drawLeftLeg()

        # Determine Victory
        if game.determineVictory() is True:
            if gui.victoryScreen(game.getFinalWord()) is True:
                game.newGame()
                gui.newGame("background.png", game.getCurrentWord())
            else:
                gui.endGame()
                break

        # Determine Lose
        if game.determineLose() is True:
            result = gui.loseScreen(game.getFinalWord())
            print(result)
            if result is True:
                print("here")
                game.newGame()
                gui.newGame("background.png", game.getCurrentWord())
            else:
                print("here2")
                gui.endGame()
                break
