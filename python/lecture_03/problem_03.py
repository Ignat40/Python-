numbers = [18, 32, 72, 100, 7, 74, 17, 45, 42, 66, 86, 79, 23, 54, 35]
min = numbers[0]
max = numbers[0]

def find_min_max(min, max):

    for i in numbers:
        if i < min:
            min = i
        if i > max:
            max = i

    print("Min: ", min)
    print("Max: ", max)

find_min_max(min, max)