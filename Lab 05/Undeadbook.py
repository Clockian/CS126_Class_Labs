# Made by Jasque Saydyk and Tyler Smith
# Lab 05 - Undeadbook
# Section 2, Feb. 22, 2017
# Description - [TODO]

# Imports
import time

# Data Structure
# Dictionary with a dictionary inside of it containg data for thing
book = {}

def update(book, status, audience, name):
    """
    Adds the post to the book, outputs the username and timestamp
    :param book: Data structure to add post to
    :param status: The text of a status update
    :param audience: A list of audiences that may be interested
    :param name: The handle/name of the person posting
    :return: A unique ID for the post that was added to book. Consists
             of username, then timestamp
    """
    currentTime = int(time.time())
    uniqueID = name + str(currentTime)

    # Dictionary inside of like, number of likes, and new key values of people who already liked
    book[uniqueID] = {"Status" : status,
                      "Audience" : audience,
                      "Name" : name,
                      "Like" : {"Likes" : 0},
                      "Unlike" : {"Unlikes" : 0}}
    print("Post made at " + str(currentTime) + " by " + name)
    return uniqueID

def like(book, id, name):
    """
    Registers a like similar to Facebook, multiple likes after the first are
    ignored
    :param book: Data structure to add post to
    :param id: ID of the post to like
    :param name: The handle/name of the person liking
    :return: Nothing
    """
    post = book[id]
    post_like = post["Like"]
    
    numberOfLikes = post_like["Likes"]
    numberOfLikes = numberOfLikes + 1
    post_like["Likes"] = numberOfLikes
    

def unlike(book, id, name):
    """
    Registers an unlike similiar to Facebook. Separate number from a like.
    Multiple unlikes are ignored
    :param book: Data structure to add post to
    :param id: ID of the post to unlike
    :param name: The handle/name of the person unliking
    :return: Nothing
    """
    post = book[id]
    post_unlike = post["Unlike"]
    
    numberOfUnlikes = post_unlike["Unlikes"]
    numberOfUnlikes = numberOfUnlikes + 1
    post_unlike["Unlikes"] = numberOfUnlikes


def display(book, id):
    """
    Displays the post associated with the unique ID, outputs a tweet like
    format
    :param book: Data structure to read post from
    :param id: ID of the post to be displayed
    :return: Nothing
    """
    print("Time: " + str(int(time.time())))
    post = book[id]
    print("Groups: " + str(post["Audience"]))
    like = post["Like"]
    print("Likes: " + str(like["Likes"]))
    print(str(post["Name"]) + " says " + str(post["Status"]))
    
"""
something = update(book,
                   "status something",
                   ["audiecne1", "audience2"],
                   "MyName")
print(something)

print(book[something])
display(book, something)
"""

# Initialize your empty 'book' variable before running the code below.

# BarnabasCollins is adding the first post to the book variable. The posted
#     says 'Storming the village at 9. Anyone interested?', and is intended
#     for the Zombie and Vampire audiences.
barnabas_one = update(book,
                      "Storming the village at 9.  Anyone interested?",
                      ["Zombies", "Vampires"],
                      "BarnabasCollins")
# some time goes by
time.sleep(1)

# Casper posts asking the vampires if he can come along.
casper_one = update(book,
                    "Can I come?",
                    ["Vampires"],
                    "Casper")
time.sleep(1)

barnabas_two = update(book,
                      "Forgot to include the ghosts! LOL",
                      ["Ghosts"],
                      "BarnabasCollins")
time.sleep(1)

barnabas_three = update(book,
                        "Lots of villagers with forks here..",
                        ["Vampires", "Zombies", "Ghosts"],
                        "BarnabasCollins")

# Edmund and Grimm like Barnabas' first post
like(book, barnabas_one, "Edmund")
like(book, barnabas_one, "Grimm")
like(book, barnabas_one, "Edmund")

# 4 different undead people like Capser's first post
like(book, casper_one, "Edmund")
like(book, casper_one, "Grimm")
like(book, casper_one, "Harry")
like(book, casper_one, "Count Chocula")

# Casper likes Barnabas' second post
like(book, barnabas_two, "Casper")

# more likes...
like(book, barnabas_three, "Casper")
like(book, barnabas_three, "Count Chocula")
like(book, barnabas_three, "Boo")

# unlikes....
unlike(book, casper_one, "Edmund")
unlike(book, barnabas_three, "Casper")
unlike(book, casper_one, "Edmund")

# display some of the posts
display(book, barnabas_one)
display(book, barnabas_three)
print("___________")
display(book, casper_one)

