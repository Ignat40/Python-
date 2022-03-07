year = int(input("Enter year to check if it is leap:"))

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        print ("The year is leap!")
    else:
        print("The year is common...")


is_leap(year)