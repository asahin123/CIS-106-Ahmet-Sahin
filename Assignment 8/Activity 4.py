# This program demonstrates while loop counting using the Fibonacci sequence based on a given number of iterations entered by the user.

# References:https://www.youtube.com/watch?v=TeFiW-2kvTY

print("Enter an iteration number")
iterationNumber = int(input())
fibonacci = [0] * (iterationNumber + 2)

fibonacci[0] = 0
fibonacci[1] = 1
count = 0
while count < iterationNumber:
    fibonacci[count + 2] = fibonacci[count + 1] + fibonacci[count]
    count = count + 1
for i in range(0, iterationNumber + 1 + 1, 1):
    print(fibonacci[i])

# References:https://www.youtube.com/watch?v=TeFiW-2kvTY
