# Write a python function that checks if a number (int) 
# can be found in a list of numbers (ints). 
# Write a python program
# that uses the function with these arguments and prints the result for each of them.


numbers = [-26, 46, 47, 5, -37, -12, 41, -8, -5, -4, -12, -34, -31, -6, 14, 19, 26, 28, 50, 45]

number = int(input("Enter the number you are looking for: "))


def contains(list_of_numbers: list, number) -> bool:
    for n in list_of_numbers:
        if n == number:
            return True

    return False


   
print(contains(numbers, number))
