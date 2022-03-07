numbers = [13, 17, 85, 49, 66, 25, 46, 65, 4, 23, 3, 71, 44, 12, 50, 62, 33, 82, 47, 36]
max = numbers[0]
second_biggest = numbers[0]

for i in numbers:
    if i > max:
        max = i
    elif second_biggest < i <= max:
        second_biggest = i

print(second_biggest)