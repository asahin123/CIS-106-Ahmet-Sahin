# This program demonstrates while loop counting using the Fibonacci sequence based on a given number of iterations entered by the user.

# References:https://www.youtube.com/watch?v=TeFiW-2kvTY

def displayFibonacciSequence(fibonacciNext):
    print(fibonacciNext)

def getValue():
    print("How many Fibonacci numbers you want to see?")
    numbersOfElement = int(input())
    
    return numbersOfElement

def whileLoop(iterationNumber):
    count = 1
    fibonacci0 = 0
    fibonacci1 = 1
    print("Fibonacci Sequence")
    displayFibonacciSequence(fibonacci0)
    displayFibonacciSequence(fibonacci1)
    while count <= iterationNumber:
        fibonacciNext = fibonacci1 + fibonacci0
        displayFibonacciSequence(fibonacciNext)
        fibonacci0 = fibonacci1
        fibonacci1 = fibonacciNext
        count = count + 1

# Main
iterationNumber = getValue() - 2
whileLoop(iterationNumber)

