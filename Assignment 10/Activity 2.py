# This program demonstrates that allows the user to think of a number between 0 and 100, inclusive. Then have the program try to guess the user’s number. Start at the midpoint (50) and ask the user if their number is (h)igher, (l)ower, or (e)qual to the guess.

# References:https://www.youtube.com/watch?v=TjkJQly2YCw

def displayCount(count):
    print("After" + str(count) + " Ali")

def displayGameIntroduction():
    print("Please, think of a number between 0 and 100, inclusive.")

def displayQuestion(value):
    print("Is the number in your mind (H)igher than, (L)ower than or (E)qual to " + str(value) + " Choose H, L or E.")

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
        if guess == "L" or guess == "l":
            higherValue = value
            value = value - (higherValue - lowerValue) / 2
        else:
            if guess == "H" or guess == "h":
                lowerValue = value
                value = value + (higherValue - lowerValue) / 2
        if not(guess != "e"): break   #Exit loop
    
    return count

# Main
count = 0
displayGameIntroduction()
count = guessingNumber(count)
displayCount(count)

