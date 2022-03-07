number = int(input("Enter value: "))

def fig(number):
    if number < 3:
        print("Please, enter bigger number...")
    elif number > 20: 
        print("Please, enter smaller number...")
    else:
        for i in range(0, number):
            if i == 0 or i == number - 1:
                print('*' * (i + 1), end = '')
            else:
                print('*', end = '')
                print('.' * (i - 1), end = '')
                print('*', end = '')
            print('')



fig(number)
            