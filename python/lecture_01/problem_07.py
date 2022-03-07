mark = float(input("Input number: "))


def valid_mark(mark):
    if 6.0 >= mark >= 5.5:
        print("Отличен")
    elif 5.5 > mark >= 4.5:
        print("Мн. Добър")
    elif 4.5 > mark >= 3.5:
        print("Добър")
    elif 3.5 > mark >= 3.0:
        print("Среден")
    elif 3.0 > mark >= 2.0:
        print("Слаб")
    else:
        print("Error - the provided number is invalid")

valid_mark(mark)