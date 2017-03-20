# Made by Jasque Saydyk and Blake Yamamoto
# Lab 06 - Banners
# Section 2, Mar. 20, 2017
# Description - Creates a method that prints
# a sentance as a bunch of ASCII characters

a = ["#####",
     "#   #",
     "#####",
     "#   #",
     "#   #"]

b = ["#### ",
     "#   #",
     "###  ",
     "#   #",
     "#### "]

c = [" ### ",
     "#   #",
     "#    ",
     "#   #",
     " ### "]

d = ["###  ",
     "#  # ",
     "#   #",
     "#  # ",
     "###  "]

e = ["#####",
     "#    ",
     "###  ",
     "#    ",
     "#####"]

f = ["#####",
     "#    ",
     "###  ",
     "#    ",
     "#    "]

g = [" ####",
     "#    ",
     "#  ##",
     "#   #",
     " ### "]

h = ["#   #",
     "#   #",
     "#####",
     "#   #",
     "#   #"]

i = ["#####",
     "  #  ",
     "  #  ",
     "  #  ",
     "#####"]

j = ["    #",
     "    #",
     "    #",
     "#   #",
     " ### "]

k = ["#   #",
     "# #  ",
     "##   ",
     "# #  ",
     "#   #"]

l = ["#    ",
     "#    ",
     "#    ",
     "#    ",
     "#####"]

m = ["#   #",
     "## ##",
     "# # #",
     "#   #",
     "#   #"]

n = ["#   #",
     "##  #",
     "# # #",
     "#  ##",
     "#   #"]

o = [" ### ",
     "#   #",
     "#   #",
     "#   #",
     " ### "]

p = ["#### ",
     "#   #",
     "#### ",
     "#    ",
     "#    "]

q = [" ### ",
     "#   #",
     "#   #",
     "# # #",
     " ## #"]

r = ["#### ",
     "#   #",
     "#### ",
     "#  # ",
     "#   #"]

s = [" ### ",
     "#    ",
     "  #  ",
     "    #",
     " ### "]

t = ["#####",
     "  #  ",
     "  #  ",
     "  #  ",
     "  #  "]

u = ["#   #",
     "#   #",
     "#   #",
     "#   #",
     " ### "]

v = ["#   #",
     "#   #",
     "#   #",
     " # # ",
     "  #  "]

w = ["#   #",
     "#   #",
     "# # #",
     "## ##",
     "#   #"]

x = ["#   #",
     " # # ",
     "  #  ",
     " # # ",
     "#   #"]

y = ["#   #",
     " # # ",
     "  #  ",
     "  #  ",
     "  #  "]

z = ["#####",
     "   # ",
     "  #  ",
     " #   ",
     "#####"]

space = ["     ",
         "     ",
         "     ",
         "     ",
         "     "]


def print_banner(sentence, alignment):
    """
    Prints the sentence as special banner ASCII characters
    :param sentence: String to be converted to banner characters
    :param alignment: 0 is horizontal, 1 is vertical
    """
    alphabet = {"A": a, "B": b, "C": c, "D": d, "E": e, "F": f, "G": g,
                "H": h, "I": i, "J": j, "K": k, "L": l, "M": m, "N": n,
                "O": o, "P": p, "Q": q, "R": r, "S": s, "T": t, "U": u,
                "V": v, "W": w, "X": x, "Y": y, "Z": z, " ": space}

    # Convert all the letters to uppercase to partially sanitize input
    sentence = sentence.upper()

    # Variables for horizontal printing
    ii = 0
    max_ascii_lines = 5

    # Print Horizontal
    if alignment == 0:
        while(ii < max_ascii_lines):
            ascii = []
            for letter in sentence:
                data = alphabet[letter]
                ascii.append(data[ii])
            for row in ascii:
                print(row, end="\t")
            print()
            ii += 1

    # Print Vertical
    else:
        for letter in sentence:
            data = alphabet[letter]
            for row in alphabet[letter]:
                print(row)
            print()

# Test
print_banner("hI gUy DudE", 0)
print()
print_banner("Hi GuY dUDe", 1)
