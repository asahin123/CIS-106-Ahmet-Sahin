# This program demonstrates while loop counting using the Fibonacci sequence based on a given number of iterations entered by the user.

# References:https://www.youtube.com/watch?v=TeFiW-2kvTY

def displayFibonacciSequence(fibonacciNext):
    print(fibonacciNext)

def forLoop(iterationNumber):
    fibonacci0 = 0
    fibonacci1 = 1
    displayFibonacciSequence(fibonacci0)
    displayFibonacciSequence(fibonacci1)
    for i in range(1, iterationNumber + 1, 1):
        fibonacciNext = fibonacci1 + fibonacci0
        displayFibonacciSequence(fibonacciNext)
        fibonacci0 = fibonacci1
        fibonacci1 = fibonacciNext

def getIterationNumber():
    print("How many Fibonacci numbers you want to see?")
    iterationNumber = int(input())
    iterationNumber = iterationNumber - 2
    print("Fibonacci Sequence")
    
    return iterationNumber

# Main
iterationNumber = getIterationNumber()
forLoop(iterationNumber)
