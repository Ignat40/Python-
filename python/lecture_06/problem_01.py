# Write a python function that returns the maximum number between three arguments.
# Write a python program that uses the function with these arguments and prints the result for each.




def maximum(x: int, y: int, z: int) -> int:
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

print(maximum(10, 20, 30))
print(maximum(12, -42, 8))
print(maximum(5, 72, -7))
print(maximum(30, 12, 72))