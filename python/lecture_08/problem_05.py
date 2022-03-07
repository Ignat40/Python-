#Write a Python class named Point constructed by an x and y coordinates. 
# Write a Python class named Circle constructed by a radius and a center Point (x, y) 
# and add the following methods:
# area() - returns the area of the circle
# perimeter() - returns the perimeter of the circle
# distance(p: Point) - returns the distance from the center to a Point passed as an argument
# position(p: Point) - returns one of the p is in the circle, 0 if it's on the edge and -1 if it's outsid


class Point:
    def __init__(self, x:float, y:float):
        self.x = x 
        self.y = y

    def display(self):
        print("x: " + str(self.x) + " y: " + str(self.y))


class Circle:
    def __init__(self, radius:float, center: Point):
        self.r = radius
        self.center = center 

    def area(self):
        return 3.14 * self.r ** 2

    def perimeter(self):
        return self.r * 2 * 3.14

    def distance(self, p: Point):
        a = self.center - p.x
        b = self.center - p.y

    def poistion(self, p: Point):
        distance = self.distance(p)

        if distance < self.r:
            return  1
        elif distance == self.r:
            return 0
        else:
            return -1

if __name__ == '__main__':

    p = Point(3, 4)
    p.display()

    c = Circle(5, 3)
    print(c.area())
    print(c.perimeter())
    c.distance(p)
    c.poistion(p)
    


    
