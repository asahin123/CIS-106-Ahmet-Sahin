# This program demonstrates while loop counting using the Fibonacci sequence based on a given number of iterations entered by the user.

# References:https://www.youtube.com/watch?v=TeFiW-2kvTY

def forLoop(iterationNumber):
    fibonacci0 = 0
    fibonacci1 = 1
    print(fibonacci0)
    print(fibonacci1)
    for i in range(1, iterationNumber + 1, 1):
        fibonacciNext = fibonacci1 + fibonacci0
        print(fibonacciNext)
        fibonacci0 = fibonacci1
        fibonacci1 = fibonacciNext

def getIterationNumber():
    print("Enter an iteration number")
    iterationNumber = int(input())
    
    return iterationNumber

# Main
iterationNumber = getIterationNumber()
forLoop(iterationNumber)
