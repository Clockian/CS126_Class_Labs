# Made by Jasque Saydyk and Oshan Vinod Wijesooriya
# Lab 04 - Grade Calculator
# Section 2, Feb. 15, 2017
# Description - This is a simple grade calculator that
# using a set predefined set of methods

# Data
homeworkScore = [39, 40, 29, 40, 0, 5]
homeworkMax = [40, 40, 40, 40, 40, 5]
homeworkWeight = 0.2

quizScore = [10, 10, 9, 2, 10, 10, 10]
quizMax = [10, 10, 10, 10, 10, 10, 10]
quizWeight = 0.2

testScore = [293, 284, 300]
testMax = [300, 300, 300]
testWeight = 0.6


def percentage_per_category(score_list, max_list):
    """
    Calculates the percentage of possible points earned in a category.
    Parameters:
        score_list - A list of points earned.
        max_list - A list of maximum possible points. Should the be same length
        as score_list
    Return:
        returns a floating point number representing the percentage of points
        earned in the given category.
    """
    numerator = sum(score_list)
    denominator = sum(max_list)
    return ((numerator/denominator) * 100)


def letter_grade(percent):
    """
    Return the letter grade of the given percentage.
    Parameters:
        percent - A floating point number from 0 to 1, representing your
        percentage score.
    Returns:
        The string "A", "B", "C", "D", "F" depending on the percentage, at
        the 90%, 80%, 70%, 60% thresholds.
    """
    if percent >= 90:
        return "A"

    elif percent >= 80:
        return "B"

    elif percent >= 70:
        return "C"

    elif percent >= 60:
        return "D"

    else:
        return "F"


def weighted_score(percentage, weight):
    """
    Calculates the weighted contribution of a category to the overall
    course grade.
    Parameters:
        percentage - The percentage of possible points earned in this
        category.
        weight - A number between 0 and 1 representing the weight of
        this category.
    Return:
        returns a floating point number representing the amount the
        given category contributes to the overall grade.
    """
    return (percentage * weight)


def to_percent(score_list, max_list):
    """
    This is a trick I learned when working in Scheme. If you've gotta
    do a recursive function, but don't have enough parameters to make
    it work? Make another function and call it in the original.
    """
    return to_percent_full(score_list, max_list, [])


def to_percent_full(score_list, max_list, percent_list):
    """
    Creates a list that contains percents of score and max list. This
    method was created because the given method signature didn't have
    enough parameters to make the recursion work
    Parameters:
        score_list - A list of points earned.
        max_list - A list of maximum possible points. Should be the
        same length as score_list.
    Return:
        A new list the same length as the input lists. Each value is
        the score's percentage of the max for that particular index.
    """
    temp1 = score_list.pop(0)
    temp2 = max_list.pop(0)

    temp = int((temp1 / temp2) * 100)
    percent_list.append(temp)

    if len(score_list) == 0:
        return percent_list
    else:
        return to_percent_full(score_list, max_list, percent_list)


def median(score_list, max_list):
    """
    Finds the middlest score of the list. Adds the biggest and
    smallest number, then divides it by two
    Parameters:
        score_list - A list of points earned.
        max_list - A list of maximum possible points. Should be the
        same length as score_list
    Return:
        The median percentage score of the inputs.
    """
    median_list = to_percent(score_list, max_list)

    median_list.sort()
    min_percent = median_list[0]
    max_percent = median_list[len(median_list) - 1]

    median_percent = int((min_percent + max_percent) / 2)
    return median_percent


# Print the percentages and letter grade for each category, and the final
# weighted score and letter grade. Round the averages to the nearest percent
homeworkPercent = percentage_per_category(homeworkScore, homeworkMax)
homeworkTotal = weighted_score(homeworkPercent, homeworkWeight)
homeworkMedian = median(homeworkScore, homeworkMax)
print("Homework Grade: " + str(int(homeworkPercent)) + "%, Grade: " +
      letter_grade(homeworkPercent) + ", Median: " + str(homeworkMedian) + "%")

quizPercent = percentage_per_category(quizScore, quizMax)
quizTotal = weighted_score(quizPercent, quizWeight)
quizMedian = median(quizScore, quizMax)
print("    Quiz Grade: " + str(int(quizPercent)) + "%, Grade: " +
      letter_grade(quizPercent) + ", Median: " + str(quizMedian) + "%")

testPercent = percentage_per_category(testScore, testMax)
testTotal = weighted_score(testPercent, testWeight)
testMedian = median(testScore, testMax)
print("    Test Grade: " + str(int(testPercent)) + "%, Grade: " +
      letter_grade(testPercent) + ", Median: " + str(testMedian) + "%")

finalScore = homeworkTotal + quizTotal + testTotal
print("   Final Score: " + str(int(finalScore)) + "%, Grade: " +
      letter_grade(finalScore))
