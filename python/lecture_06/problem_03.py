# Write a python function that reverses and returns a number (positive int). 
# Write a python program that uses the function 
# with these arguments and prints the result for each of them.

n = int(input("Enter the number you want to reverse:"))

def reverse_number(n):
    result = 0

    while n != 0:
        result = result * 10 + n % 10
        n = n//10

    return result

print("Reversed", reverse_number(n))