x = int(input("Enter value for x:"))
y = int(input("Enter value for y:"))


def is_greater(x, y):
    if x > y:
        print("X is greater than Y")
    elif x < y:
        print("X is less than Y")
    elif x == y:
        print("X is equal to Y")


is_greater(x, y)
