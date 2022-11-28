# This program displays high, low,
# and average scores based on input from scores.txt.

# References:https://youtu.be/Uh2ebFW8OYM

def display_result(list_scores, max, min, ave):
    print()
    print("Score List : ")
    print(list_scores)
    print()
    print("Maximum Score : {0:.2f}".format(max))
    print("Minimum Score : {0:.2f}".format(min))
    print("Average Score : {0:.2f}".format(ave))


def read_file(filename):
    try:
        with open(filename, "r") as file:
            list_scores = []
            for line in file:
                lines = line.strip().split(",")
                line1 = lines[1]
                if line1.isnumeric():
                    list_scores.append(int(lines[1]))
            return list_scores
    except Exception as exception:
        print(exception)


def file_process(list_scores):
    summation = 0
    for score in list_scores:
        summation = summation + int(score)
    max_value = max(list_scores)
    min_value = min(list_scores)
    average = summation / len(list_scores)
    display_result(list_scores, max_value, min_value, average)


def main():
    filename = "scores.txt"
    list_scores = read_file(filename)
    file_process(list_scores)

main()


