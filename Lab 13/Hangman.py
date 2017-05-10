# Made by Jasque Saydyk
# Lab 13 - Hangman
# Section 2, May 8, 2017
# Description - Contains the game logic for Hangman
import random


class Hangman:

    _maxBadChoices = 6
    _badChoices = 0
    _wordList = []
    _usedLetters = []
    _finalWord = ""
    _currentWord = ""

    def __init__(self, file):
        """
        Sets up initial variables, fills currentWord as a bunch of zeros
        """
        self.readWords(file)
        self.chooseWord()

    def getFinalWord(self):
        return self._finalWord

    def getCurrentWord(self):
        return self._currentWord

    def getUsedLetters(self):
        return self._usedLetters

    def getBadChoices(self):
        return self._badChoices

    def readWords(self, file):
        """
        Transfers words in a file to a usable data structure
        :param file: Open file stream of words
        """
        for nextline in file:
            self._wordList.append(nextline)

    def chooseWord(self):
        """
        Randomly chooses a word from the given words
        """
        random.shuffle(self._wordList)
        self._finalWord = self._wordList[0]
        for i in range(len(self._finalWord) - 1):
            self._currentWord += "_"

    def inputLetter(self, letter):
        """
        Takes received letter, determines if it fits in the word, doesn't fit,
        or if it has already been given, and either adds it to the word or
        adds to badChoices
        :param letter: Single letter to determine if it exists in the finalWord
        :raises ValueError: Given an invalid input that is not a
            single alphabet letter or has already been given
        :return: True if the letter exists in finalWord, False if not
        """
        if len(letter) > 1:
            raise ValueError("Letter is not a single character")
        if self.determineLetterRepeat(letter) is True:
            raise ValueError("Letter has already been entered")
        if self.determineLetterMatch(letter) is True:
            self.updateLetterInWord(letter)
            self._usedLetters.append(letter)
            return True
        else:
            self._usedLetters.append(letter)
            self._badChoices += 1
            return False

    def determineLetterMatch(self, letter):
        """
        Determines if the letter belongs in the word or not
        :param letter: Single letter to determine if it exists in the finalWord
        :return: True if the letter belongs, False if not
        """
        if letter in self._finalWord:
            return True
        else:
            return False

    def determineLetterRepeat(self, letter):
        """
        Determines if the letter has already been used in the program
        :param letter: Single letter to determine if it exists in the finalWord
        :return: True if the letter is a repeat, False if not
        """
        if letter in self._usedLetters:
            return True
        else:
            return False

    def updateLetterInWord(self, letter):
        """
        Updates the letter in the currentWord in all of the applicable spots
        :param letter: Single letter to determine if it exists in the finalWord
        """
        finalWordList = list(self._finalWord)
        for index, wordLetter in enumerate(finalWordList):
            if letter is wordLetter:
                temp = list(self._currentWord)
                temp[index] = letter
                self._currentWord = "".join(temp)

    def determineVictory(self):
        """
        Determines if a victory condition has been met or not. Victory entails
        the word being completely filled out without reaching the max number of
        badChoices.
        :return: True if victory has been achieved, False otherwise
        """
        currentWordList = list(self._currentWord)
        result = True
        for wordLetter in currentWordList:
            if wordLetter == "_":
                result = False

        if result is True:
            return True
        else:
            return False

    def determineLose(self):
        """
        Determines if a game as entered a lose state and must reset
        :return: True if game has been lost and must end or restart, False if
            otherwise
        """
        if self._badChoices == self._maxBadChoices:
            return True
        else:
            return False

    def newGame(self):
        """
        Clears all of the neccesary variables and sets up a new game of Hangman
        """
        self._badChoices = 0
        self._usedLetters = []
        self._finalWord = ""
        self._currentWord = ""
        self.chooseWord()
