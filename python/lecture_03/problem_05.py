numbers = [68, 65, 30, 87, 21, 17, 96, 70, 64, 34, 14, 90, 86, 31, 29, 40, 59, 23, 25, 95, 60, 85, 42, 37, 57, 18, 27,
           77, 36, 75, 4, 5, 38, 63, 76, 81, 53, 24, 62, 98, 83, 55, 67, 1, 7, 92, 8, 51, 52, 61, 3, 56, 97, 12, 71, 20,
           16, 26, 50, 10, 73, 89, 88, 49, 28, 100, 13, 47, 69]

number = int(input("Enter the number you are looking for: "))
found = False

for i in numbers:
    if i == number:
        found = True
        break

if found:
    print("Number found")
else:
    print("Not found...")