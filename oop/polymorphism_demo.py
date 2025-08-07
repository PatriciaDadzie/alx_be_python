import math

# Shape class
class Shape:
    def area(self):
        # This method is meant to be overridden by subclasses
        raise NotImplementedError("Subclasses must implement the area method.")


# Derived Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
