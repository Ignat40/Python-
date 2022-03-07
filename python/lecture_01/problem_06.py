nubmer = int(input("Enter value for the number: "))

def is_wierd(number):
    if number % 2 == 0:  
        print("Wierd")
    elif 16 < number < 32:
        print("Wierd")
    elif 64 < number < 128:
        print("Wierd")
    elif number % 5 == 0:
        print("Wired")
    else:
        print ("Not wierd")
        

is_wierd(nubmer)