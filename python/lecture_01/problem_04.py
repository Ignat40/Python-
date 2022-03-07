from python.lecture_01.problem_03 import find_max


x = int(input("Enter value for x:"))
y = int(input("Enter value for y:"))
z = int(input("Enter value for z:"))

def smallest(x, y, z):
    if x < z and x < y:
        print("The smallest number is:", x)
    elif y < z and y < x:
        print("The smallest number is:", y)
    else:
        print("The smallest number is:", z)


smallest(x,z,y)