numbers_01 = [13, 17, 85, 49, 66, 25, 46, 65, 4, 23, 3, 71, 44, 12, 50, 62, 33, 82, 47, 36]
numbers_02 = [89, 75, 78, 84, 27, 82, 63, 72, 6, 41, 77, 35, 92, 90, 8, 72, 21, 74, 48, 97, 42, 28, 45, 84, 22, 63, 4,
              74, 6, 70, 13, 30]
numbers_03 = [54, 32, 37, 35, 66, 48, 15, 27, 48, 82, 38, 96, 58, 95, 13, 64, 67, 58, 94, 90, 10, 11, 36, 29, 36, 25,
              20, 94, 25, 74, 42, 30, 74, 52, 12, 39, 70, 30, 14, 91, 92, 55, 11, 6, 55, 36, 92, 84, 11, 90, 76, 11, 18,
              32, 1, 16, 73, 66, 21, 86, 49, 53, 33, 25]
numbers_04 = [68, 65, 30, 87, 21, 17, 96, 70, 64, 34, 14, 90, 86, 31, 29, 40, 59, 23, 25, 95, 60, 85, 42, 37, 57, 18,
              27, 77, 36, 75, 4, 5, 38, 63, 76, 81, 53, 24, 62, 98, 83, 55, 67, 1, 7, 92, 8, 51, 52, 61, 3, 56, 97, 12,
              71, 20, 16, 26, 50, 10, 73, 89, 88, 49, 28, 100, 13, 47, 15]

is_duplicate = False
lens = len(numbers_01)
leng = len(numbers_02)
lengh = len(numbers_03)
lenght = len(numbers_04)

for i in range(lens):
    for j in range(lens):
        if i != j and numbers_01[i] == numbers_01[j]:
            is_duplicate = True

for i in range(leng):
    for j in range(leng):
        if i != j and numbers_02[i] == numbers_02[j]:
            is_duplicate = True

for i in range(lengh):
    for j in range(lengh):
        if i != j and numbers_03[i] == numbers_03[j]:
            is_duplicate = True

for i in range(lenght):
    for j in range(lenght):
        if i != j and numbers_04[i] == numbers_04[j]:
            is_duplicate = True


if is_duplicate:
    print("Duplicats found")
else:
    print("The list is free of duplicates")
if is_duplicate:
    print("Duplicats found")
else:
    print("The list is free of duplicates")
if is_duplicate:
    print("Duplicats found")
else:
    print("The list is free of duplicates")
if is_duplicate:
    print("Duplicats found")
else:
    print("The list is free of duplicates")