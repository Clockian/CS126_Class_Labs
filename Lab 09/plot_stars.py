# Made by Jasque Saydyk and Isai Martinez
# Lab 09 - Draw Stars
# Section 2, April 12, 2017
# Description - Draws the coordinates of a bunch of stars with a given
# file, using turtle
from turtle import *


def read_coords(file):
    """
    Creates three dictionaies containing star data from given file stream
    Dictionary 1 - key, Henry Draper number, value, tuples containing x
        and y cooridinates of each star
    Dictionary 2 - key, Henry Draper number, value, magnitude(float) of
        the star
    Dictionary 3 - key, name of the stars, value, it's Henry Draper
        numbers, stars
        with no name are not represented
    :param file - Open file stream of star coordinates
    :return - Tuple of the three dictionarys containing star data
    """
    coordinates_dict = {}
    magnitude_dict = {}
    name_dict = {}

    for nextLine in file:
        s = nextLine.split()
        henry_draper_num = s[3]
        coordinates = (s[0], s[1])
        coordinates_dict[henry_draper_num] = coordinates
        magnitude_dict[henry_draper_num] = s[4]

        # If the star has a name
        word_holder = [""]
        ii = 0
        new_name = True
        # Start if list has names
        if len(s) > 6:
            # Pull out the potentially multiple names into list contain
            # name for each index
            for word in s[5:]:
                if ';' in word:
                    new_word = word.replace(";", "")
                    word_holder[ii] += " "
                    word_holder[ii] += new_word
                    word_holder.append("")
                    new_name = True
                    ii += 1
                else:
                    if new_name is False:
                        word_holder[ii] += " "
                    word_holder[ii] += word
                    new_name = False

            # Put formatted names into dict
            for name in word_holder:
                name_dict[name] = henry_draper_num
    return (coordinates_dict, magnitude_dict, name_dict)


def plot_plain_stars(picture_size, coordinates_dict):
    """
    Plots the stars on a black canvas as white squares
    :param picture_size - The size of the picture or canvas in
        pixels, all black
    :param coordinates_dict - The coordinates of the different stars
        to be placed on canvas as 2x2 pixel, white filled rectangles
    """
    tracer(0)
    speed(10)

    # Get the middle of image
    center = picture_size / 2

    # Create canvas by drawing square and filling it black
    fillcolor('black')
    begin_fill()
    pu()
    setposition(-center, center)
    pd()
    for x in range(4):
        forward(picture_size)
        right(90)
    end_fill()

    # Finally, place coordinates of all the stars
    for key in coordinates_dict:
        coordinate = coordinates_dict[key]
        # Convert coordinates to be larger values, then set turtle
        converted_x = int(float(coordinate[0]) * 100)
        converted_y = int(float(coordinate[1]) * 100)
        pu()
        setposition(converted_x, converted_y)
        pd()
        # Create the star
        fillcolor('white')
        begin_fill()
        for i in range(4):
            forward(2)
            right(90)
        end_fill()


def plot_by_magnitude(picture_size, coordinates_dict, magnitudes_dict):
    """
    Similiar to plot_plain_stars(), but the stars are bigger and
    smaller according to their magnitude, which is by the equation in
    the documentation
    :param picture_size - The size of the picture or canvas in pixels,
        all black
    :param coordinates_dict - The coordinates of the different stars
        to be placed on canvas as 2x2 pixel, white filled rectangles
    :param magnitudes_dict - The magnituds of the different stars
    """
    tracer(0)
    speed(10)

    # Get the middle of image
    center = picture_size / 2

    # Create canvas by drawing square that is picture size and filling it black
    fillcolor('black')
    begin_fill()
    pu()
    setposition(-center, center)
    pd()
    for x in range(4):
        forward(picture_size)
        right(90)
    end_fill()

    # Finally, place coordinates of all the stars
    for key in coordinates_dict:
        coordinate = coordinates_dict[key]

        # Convert coordinates to be larger values, then set turtle
        converted_x = int(float(coordinate[0]) * 100)
        converted_y = int(float(coordinate[1]) * 100)
        pu()
        setposition(converted_x, converted_y)
        pd()

        # Determine the size of the star
        magnitude = float(magnitudes_dict[key])
        star_size = min(round(10.0/(magnitude + 2)), 8)

        # Create the star
        fillcolor('white')
        begin_fill()
        for i in range(4):
            forward(star_size)
            right(90)
        end_fill()


def read_constellation_lines(file):
    """
    Extra Credit(optional)
    """


def plot_constellations(pic_size, star_names, star_coords, constellations):
    """
    Extra Credit(optional)
    """


# Main of program
if __name__ == "__main__":
    filehandle = open("stars.txt", "r")
    dicts = read_coords(filehandle)
    coordinates_dict = dicts[0]
    # plot_plain_stars(220, coordinates_dict)
    plot_by_magnitude(220, coordinates_dict, dicts[1])
