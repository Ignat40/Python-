#Write a Python class named Circle constructed by a radius and two methods
#  which will compute the area and the perimeter of a circle


class Cirle:

    def __init__(self, radius):
        self.r = radius

    def area(self):
        return self.r * self.r * 3.14

    def perimenter(self):
        return self.r * 2 * 3.14

c = Cirle(5)
print(c.area())
print(c.perimenter())