#This program asks the user to enter grade scores they would 
#like to enter.After the scores are entered, calculate
#and display the high, low, and average for the entered scores.

#References:https://www.youtube.com/results?
#search_query=difference
#+between+dynamic+and+static+arrays


def display_result(max_grades, min_grades, ave_grades):
    print("Maximum Grade is " + str(max_grades))
    print("Minimum Grade is " + str(min_grades))
    print("Average Grade is " + str(ave_grades))


def get_list(grades):
    value = 0
    
    while value >= 0:
        value = get_list_value()
        if value >= 0:
            grades.append(value)
        else:
            break
    return grades


def get_list_value():
    print("Please enter the grade : ")
    grade_value = float(input())
    
    return grade_value


def get_max_grade(gradelist):
    grade_max = gradelist[0]

    for w in gradelist:
        if grade_max < w:
            grade_max = w
    
    return grade_max


def get_min_grade(gradelist):
    grade_min = gradelist[0]

    for w in gradelist:
        if grade_min > w:
            grade_min = w
    
    return grade_min


def get_average_grade(gradelist):
    grade_sum = 0
    list_size = len(gradelist)
    for w in gradelist:
        grade_sum = grade_sum + w

    average = grade_sum / list_size

    return average
 

def main()
    grade_list = []

    grades = get_list(grade_list)
    max_grade = get_max_grade(grades)
    min_grade = get_min_grade(grades)
    ave_grade = get_average_grade(grades)
    display_result(max_grade, min_grade, ave_grade)


main()
