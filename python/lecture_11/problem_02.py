class Shape(object):
    def area(self):
        raise NotImplementedError()

    def perimeter(self):
        raise NotImplementedError()

    def __str__(self):
        return type(self).__name__


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3,14 * self.radius**2

    def perimeter(self):
        return 2 * 3,14 * self.radius

class Rectangular(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

class Shquare(Rectangular):
    def __init__(self, length):
        super().__init__(length, length)

if __name__ == '__main__':

    shapes = [Shquare(10), Rectangular(5, 10), Circle(50)]

    for shape in shapes: 
        print(f"shape: {type(shape)}, area: {shape.area()}, perimeter: {shape.perimeter()}")


