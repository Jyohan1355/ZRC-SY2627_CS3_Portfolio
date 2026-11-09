from abc import ABC, abstractmethod


class Shape(ABC):
    
    @abstractmethod
    def area(self):

        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):

        return 3.14159 * (self.radius ** 2)

#  interact with the abstraction, not the complex details
my_shapes = [
    Rectangle(width=4, height=5),
    Circle(radius=3)
]


for shape in my_shapes:
    print(f"The area is: {shape.area()}")