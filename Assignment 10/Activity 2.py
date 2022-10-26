# This program demonstrates that allows the user to think of a number between 0 and 100, inclusive. Then have the program try to guess the user’s number. Start at the midpoint (50) and ask the user if their number is (h)igher, (l)ower, or (e)qual to the guess.

# References:https://www.youtube.com/watch?v=TjkJQly2YCw

def displayCount(count):
    print("After " + str(count) + " attempts, the number in your mind is found")

def displayGameIntroduction():
    print("Please, think of a number between 0 and 100, inclusive.")

def displayQuestion(value):
    print("Is the number in your mind (h)igher than, (l)ower than or (e)qual to " + str(value) + ". Choose h, l or e.")

def getACharacter():
    character = input()
    
    return character

def guessingNumber(count):
    guess = " "
    value = 50
    lowerValue = 0
    higherValue = 100
    while True:    #This simulates a Do Loop
        count = count + 1
        displayQuestion(value)
        guess = getACharacter()
        if guess == "l" or guess == "L":
            higherValue = value
            value = value - float(higherValue - lowerValue) / 2
        else:
            if guess == "h" or guess == "H":
                lowerValue = value
                value = value + float(higherValue - lowerValue + 1) / 2
        if not(guess != "e"): break   #Exit loop
    
    return count

# Main
count = 0
displayGameIntroduction()
count = guessingNumber(count)
displayCount(count)
