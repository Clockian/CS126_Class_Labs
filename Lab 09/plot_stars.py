read_coords(file):
    """
    Creates three dictionaies containing star data from given file stream
    Dictionary 1 - key, Henry Draper number, value, tuples containing x
        and y cooridinates of each star
    Dictionary 2 - key, Henry Draper number, value, magnitude(float) of the star
    Dictionary 3 - key, name of the stars, value, it's Henry Draper numbers, stars
        with no name are not represented
    :param file - Open file stream of star coordinates
    :return - Tuple of the three dictionarys containing star data
    """


plot_plain_stars(picture_size, coordinates_dict):
    """
    Plots the stars on a black canvas as white squares
    :param picture_size - The size of the picture or canvas in pixels, all black
    :param coordinates_dict - The coordinates of the different stars to be placed
        on canvas as 2x2 pixel, white filled rectangles
    """


plot_by_magnitude(picture_size, coordinates_dict, magnitudes_dict):
    """
    Similiar to plot_plain_stars(), but the stars are bigger and smaller according
    to their magnitude, which is by the equation in the documentation
    :param picture_size - The size of the picture or canvas in pixels, all black
    :param coordinates_dict - The coordinates of the different stars to be placed
        on canvas as 2x2 pixel, white filled rectangles
    :param magnitudes_dict - The magnituds of the different stars
    """


read_constellation_lines(file):
    """
    Extra Credit(optional)
    """


plot_constellations(pic_size, star_names, star_coords, constellations):
    """
    Extra Credit(optional)
    """

    
