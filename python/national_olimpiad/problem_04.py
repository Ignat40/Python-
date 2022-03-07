number = int(input("Enter value for the number: "))

def add_digits(nubmer):

    sum = 0
    if number < 100:
        print("Please enter larger number: ")
    elif number > 9999:
        print("Please enter smaller number: ")
    else:
        for i in str(number):
            sum += int(i)
        print(sum)


add_digits(number)