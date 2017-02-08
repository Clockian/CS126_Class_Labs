from random import randint

correct = 0
for i in range(10):
    n1 = randint(1, 8)
    n2 = randint(1, 8)
    prod = n1 * n2

    ans = input("What's %d times %d? " % (n1, n2))
    if int(ans) == prod:
        print("That's right ----- well done.\n")
        correct = correct + 1
    else:
        print("No, I'm afraid the answer is %d.\n" % prod)
print("\nI asked you 10 questions. You go %d of them right." % correct)
print("Well done!")
