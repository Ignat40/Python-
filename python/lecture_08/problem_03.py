#Wrtie a python class named Recatangle constructed by a lenght and width 
# and a method whick will compyute the area of a rectangle



class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.width * self.length


if __name__ == '__main__':

    shape = Rectangle(5, 10)
    print(shape.area())