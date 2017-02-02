#Made by Jasque Saydyk
#Proof of Concept for Lab 2
end = False

while(end == False):
    print("\nYou awaken from your bed, feeling strange.")
    print("Something is going to happen today, something")
    print("big, but you don’t know what….")
    choice = input("Do you STAY, GET UP, or YAWN? ")
    
    if(choice == "STAY"):
        print("\nFeeling tired, you go to get a couple more moments of sleep")
        print("As you cuddle up, you feel the bed is warm…. And moist….")
        print("As you look up, you realize in horror that you are eaten by a Bedoster")
        while(end == False):
            choice = input("Try Again? YES/NO: ")
            if(choice == "NO"):
                end = True
            elif(choice == "YES"):
                break
            else:
                print("\nERROR: Enter one of the all-cap words in all-cap")
                
    elif(choice == "GET UP"):
        print("\nYou get up, the carpet tickles your feet. You then fall to the ground laughing at how much the")
        print("Carpet tickles you. As you laugh, you realize you cannot breath in")
        print("You die, with a smile on you face on the carpet")
        while(end == False):
            choice = input("Try Again? YES/NO: ")
            if(choice == "NO"):
                end = True
            elif(choice == "YES"):
                break
            else:
                print("\nERROR: Enter one of the all-cap words in all-cap")

    elif(choice == "YAWN"):
        print("You sit up, stretch and let out an uplifting yawn that dispels the sleep from your body")
        print("You get out of bed, putting on your normal clothes, then approach the stairs")
        print("By the stairs, you see an old family chest you haven’t opened in years…")
        while(end == False):
            choice = input("Do you DESCEND, INVESTIGATE, or STAY? ")
            print("\nNO CODE!!!!")
            end = True
    
    else:
        print("\nERROR: Enter one of the all-cap words in all-cap")
