# Made by Jasque Saydyk and Oshan Vinod Wijesooriya
# Lab 04 - Grade Calculator
# Section 2, Feb. 15, 2017
# Description - This is a simple grade calculator that
# uses a set of methods

# Data
homeworkScore = [39, 40, 29, 40, 0, 5]
homeworkMax = [40, 40, 40, 40, 40, 5]
homeworkWeight = 0.2

quizScore = [10, 10, 9, 2, 10, 10, 10]
quizMax = [10, 10, 10, 10, 10, 10, 10]
quizWeight = 0.6

testScore = [293, 284, 300]
testMax = [300, 300, 300]
testWeight = 0.2

def percentage_per_category(score_list, max_list):
    """
    Calculates the percentage of possible points earned in a category.
    Parameters:
        score_list - A list of points earned.
        max_list - A list of maximum possible points. Should the be same length
        as score_list
    Return:
        returns a floating point number representing the percentage of points earned
        in the given category.
    """
    numerator = sum(score_list)
    denominator = sum(max_list)
    return ((numerator/denominator) * 100)

def letter_grade (percent):
    """
    Return the letter grade of the given percentage.
    Parameters:
        percent - A floating point number from 0 to 1, representing your percentage score.
    Returns:
        The string "A", "B", "C", "D", "F" depending on the percentage, at the 90%, 80%,
        70%, 60% thresholds.
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

# Todo: Double check, may not calculate correctly despite lab
def weighted_score (percentage , weight) :
    """
    Calculates the weighted contribution of a category to the overall course grade.
    Parameters:
        percentage - The percentage of possible points earned in this category.
        weight - A number between 0 and 1 representing the weight of this category.
    Return:
        returns a floating point number representing the amount the given category
        contributes to the overall grade.
    """
    return (percentage * weight)

# Todo: Extra Credit Methods
""""
def to_percent(score_list , max_list):

    for i in range(len(score_list)):

        percent[i] =( score_list[i]/max_list[i] )

    return percent
# re-check this 
def median ( score_list , max_list):

    for i in range(len(score_list)):

        percent[i] =( score_list[i]/max_list[i] )

        
    percent = sum(percent)/len(percent)
    
    return percent
"""

# Print the percentages and letter grade for each category, and the final weighted score and letter grade
# Round the averages to the nearest percent
homeworkPercent = percentage_per_category(homeworkScore, homeworkMax)
homeworkTotal = weighted_score(homeworkPercent, homeworkWeight)
print("Homework: " + str(int(homeworkPercent)) + "%, Grade: " + letter_grade(homeworkPercent) +
      ", Final Weighted Score: " + str(homeworkTotal) + ".")

quizPercent = percentage_per_category(quizScore, quizMax)
quizTotal = weighted_score(quizPercent, quizWeight)
print("Quiz: " + str(int(quizPercent)) + "%, Grade: " + letter_grade(quizPercent) +
      ", Final Weighted Score: " + str(quizTotal) + ".")

testPercent = percentage_per_category(testScore, testMax)
testTotal = weighted_score(testPercent, testWeight)
print("Test: " + str(int(testPercent)) + "%, Grade: " + letter_grade(testPercent) +
      ", Final Weighted Score: " + str(testTotal) + ".")

finalScore = homeworkTotal + quizTotal + testTotal
print("Final Score: " + str(int(finalScore)) + "%, Grade: " + letter_grade(finalScore))
