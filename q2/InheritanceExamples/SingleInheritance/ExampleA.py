# Superclass
class Shape:
  # Constructor method of superclass.
    def __init__(self):
        self.length = float(input("Enter the length: "))
        self.breadth = float(input("Enter the breadth: "))

  # Display() method of superclass.
    def display(self):
        print("Length = ", self.length)
        print("Breadth = ", self.breadth)

# Subclass.
class Rectangle(Shape):
  # Constructor method of subclass.
    def __init__(self):
      # Calling the constructor method of the superclass.
        Shape.__init__(self)

    def cal_per(self):
        self.per = 2 * (self.length + self.breadth)
        print("Perimeter of rectangle = ", self.per)

    def cal_area(self):
        self.area = self.length * self.breadth
        print("Area of rectangle = ", self.area)

# Create an object of class Rectangle.
rt = Rectangle()

# Calling method of subclass using rt.
rt.display()
rt.cal_per()
rt.cal_area()
