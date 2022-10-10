# This program demonstrates while loop counting using the Fibonacci sequence based on a given number of iterations entered by the user.

# References:https://www.youtube.com/watch?v=TeFiW-2kvTY

def forLoop(iterationNumber, fibonacci):
    for i in range(0, iterationNumber + 1 + 1, 1):
        print(fibonacci[i])

def getIterationNumber():
    print("Enter an iteration number")
    iterationNumber = int(input())
    
    return iterationNumber

def whileLoop(iterationNumber, fibonacci):
    count = 0
    while count < iterationNumber:
        fibonacci[count + 2] = fibonacci[count + 1] + fibonacci[count]
        count = count + 1

# Main
iterationNumber = getIterationNumber()
fibonacci = [0] * (iterationNumber + 2)

fibonacci[0] = 0
fibonacci[1] = 1
whileLoop(iterationNumber, fibonacci)
forLoop(iterationNumber, fibonacci)


