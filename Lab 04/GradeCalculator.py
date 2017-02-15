
homeworkScore = [39,40,40,40,29,40,0,5]
homeworkDenominator = [40,40,40,40,40,5]
quizScore = [10,10,9,2,10,10,10]
quizDenominator = [10,10,10,10,10,10,10]
testScore = [293,284,300]
testDenominator = [300,300,300]

homeworkWeight = 0.2
testWeight = 0.2
quizWeight = 0.6


def percentage_per_category(score_list, max_list):
    """Calculates the percentage of """
    
    numerator = sum(score_list)
    denominator = sum(max_list)
    return (numerator/denominator)

def letter_grade (percent):

    if percent >= 0.9:

        letter_grade = "A"
    elif percent >=0.8 :

        letter_grade = "B"

    elif percent >=0.7:

        letter_grade = "c"

    elif percent >=0.6:

        letter_grade = "D"

    else :
        letter_grade = "F"

    return letter_grade
def weighted_score (percentage , weight) :

    return (percentage * weight)

def print (category, weighted_score, letter_grade):

    print(category ," : ",weighted_score ," (",lettergrade,")")

def to_percent(score_list , max_list):

    for i for range(len(score_list)):

        percent[i] =( score_list[i]/max_list[i] )

    return percent
# re-check this 
def median ( score_list , max_list):

    for i for range(len(score_list)):

        percent[i] =( score_list[i]/max_list[i] )

        
    percent = sum(percent)/len(percent)
    
    return percent

        
    
