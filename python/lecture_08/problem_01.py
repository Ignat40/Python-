# Write a Python class named Student with two attributes student_id, student_name. 
# Create a constructor for these values. 
# Create a method display() to display the entire 
# attribute and their values in Student class.

class Student:
    def __init__(self, student_id, student_name):
        self.id = student_id
        self.name = student_name

    def display(self):
        print("ID: ", self.id)
        print("Name", self.name)


if __name__ == '__main__':

    s = Student(43, "Marian")
    s.display()