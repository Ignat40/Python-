# Write a python function that takes a string as an argument
#  and returns `True` if it is `palindrome` and `False` if not.
# Write a python program that uses the function with these 
# arguments and prints the result for each of them.


def is_palindrom(string: str) -> bool:
    for i in range(int(len(string))):
        if string[i] != string[-i -1]:
            return False

        return True


print(is_palindrom("abcdef"))
print(is_palindrom("abcdedcba"))
print(is_palindrom("12345"))
print(is_palindrom("123454321"))