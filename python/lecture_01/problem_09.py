import math

a = float(input("Enter value for a:"))
b = float(input("Enter value for b:"))
c = float(input("Enter value for c:"))


def quadratic_equations(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/2
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/2

    print(x1, x2)


quadratic_equations(a,b,c)