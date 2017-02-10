from random import randint
from random import choice

correct = 0

numberOfQuestions = int(input("How mnay Question's?"))

levelOfDifficulty = input("What difficulty do you want? (Beginner, Intermidate, Advanced) ")

# Beginner Section
if(levelOfDifficulty == "Beginner"):
    for i in range(numberOfQuestions):
        n1 = randint(1, 10)
        n2 = randint(1, 10)

        # Deciding between Plus or minus
        coinFlip = choice([1, 2])
        if(coinFlip == 1):
            questionAnswer = n1 + n2
            userAnswer = int(input("What's %d plus %d? " % (n1, n2)))
        else:
            questionAnswer = n1 - n2
            userAnswer = int(input("What's %d minus %d? " % (n1, n2)))

        # Deciding if answer is right
        if userAnswer == questionAnswer:
            print("That's right ----- well done.\n")
            correct = correct + 1
        else:
            print("No, I'm afraid the answer is %d.\n" % questionAnswer)

# Intermidate Section
elif(levelOfDifficulty == "Intermidate"):
    for i in range(numberOfQuestions):
        n1 = randint(1, 8)
        n2 = randint(1, 8)
        coinFlip = choice([1, 2, 3, 4])

        # deciding between Subtraction, Addition, Multiplication, and Division
        if(coinFlip == 1):
           questionAnswer = n1 + n2
           userAnswer = int(input("What's %d plus %d? " % (n1, n2)))
        elif(coinFlip == 2):
            questionAnswer = n1 - n2
            userAnswer = int(input("What's %d minus %d? " % (n1, n2)))
        elif(coinFlip == 3):
            questionAnswer = n1 * n2
            userAnswer = int(input("What's %d times %d? " % (n1, n2)))
        else:
            questionAnswer = n1 / n2
            userAnswer = int(input("What's %d divided by %d? " % (n1, n2)))
            

        # Deciding if answer is right
        if userAnswer == questionAnswer:
            print("That's right ----- well done.\n")
            correct = correct + 1
        else:
            print("No, I'm afraid the answer is %d.\n" % questionAnswer)

# Advanced section
elif(levelOfDifficulty == "Advanced"):
  
    coinFlip = choice([1, 2, 3, 4, 5])

    # deciding between Subtraction, Addition, Multiplication, and Division
    if(coinFlip == 1):
       questionAnswer = 1 + 2
       userAnswer = int(input("What's 1 plus 2? "))
    elif(coinFlip == 2):
        questionAnswer = n1 * n2
        userAnswer = int(input("What's 2 times 5? "))
    elif(coinFlip == 3):
        questionAnswer = 4 / 2
        userAnswer = int(input("What's 4 divide 2? "))
    elif(coinFlip == 4):
        questionAnswer = 631 - 12
        userAnswer = int(input("What's  631 - 12? "))
    else:
        questionAnswer = 4 * 20
        userAnswer = int(input("What's 4 * 20? "))
        

    # Deciding if answer is right
    if userAnswer == questionAnswer:
        print("That's right ----- well done.\n")
        correct = correct + 1
    else:
        print("No, I'm afraid the answer is %d.\n" % questionAnswer)

else:
    print("You typed bad input")



   
print("\nI asked you %d questions. You go %d of them right." % (numberOfQuestions, correct))
print("Well done!")

