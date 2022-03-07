# Write a python function that finds and returns the factorial of a number (non-negative int). Write a python program that
# uses the function with these arguments and prints the result for each of them.


f = int(input("Enter number to check its factorial: "))

def find_ficatorial(f):
    factorial = 1

    for i in range(1, f + 1):
        factorial *= i

    return factorial


print("Factorial is: ", find_ficatorial(f))