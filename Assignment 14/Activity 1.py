# This program displays high, low,
# and average scores based on input from scores.txt.

# References:https://youtu.be/Uh2ebFW8OYM

def display_result(list_scores, max, min, ave):
    print()
    print("score List : ")
    print(list_scores)
    print()
    print("Maximum score : {0:.2f}".format(max))
    print("Minimum score : {0:.2f}".format(min))
    print("Average score : {0:.2f}".format(ave))


def read_file(filename):
    try:
        with open(filename, "r") as file:
            list_scores = []
            for line in file:
                lines = line.strip().split(",") # Name,Score  ==>  ["Name","Score"]
                line1 = lines[1]
                if line1.isnumeric():
                    list_scores.append(int(lines[1]))
            return list_scores
    except Exception as exception:
        print(exception)


def calculate_minimum(list_scores):
    min_value = min(list_scores)
    return min_value


def calculate_maximum(list_scores):
    max_value = max(list_scores)
    return max_value


def calculate_average(list_scores):
    summation = 0
    for score in list_scores:
        summation = summation + int(score)
    average = summation / len(list_scores)
    return average


def main():
    filename = "scores.txt"
    list_scores = read_file(filename)
    min_value = calculate_minimum(list_scores)
    max_value = calculate_maximum(list_scores)
    ave_value = calculate_average(list_scores)
    display_result(list_scores, max_value, min_value, ave_value)


main()
