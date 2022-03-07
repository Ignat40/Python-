# Write a python function that returns the amount of numbers
#  from a list in a given range `[a, b]`. Write a python program
# that uses the function with these arguments and
#  prints the result for each of them.

list = [-26, 46, 47, 5, -37, -12, 41, -8, -5, -4, -12, -34, -31, -6, 14, 19, 26, 28, 50, 45]
a = 0
b = 100


def numbers_in_range(list: int, a: int, b: int) -> int:

    count = 0

    for i in list:
        if a <= i <= b:
            count += 1
    return count


print(numbers_in_range(list, -100, 100))
