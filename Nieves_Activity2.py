"""
Activity 2 - Rectangle class using the @property decorator
width and height are private members. The getters/setters are accessed
like regular attributes (no parentheses).
"""


class Rectangle:
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.width = width      # uses the setter (validation)
        self.height = height    # uses the setter (validation)

    # ----- width -----
    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self.__width = new_width
        else:
            print("Width must be greater than 0.")

    # ----- height -----
    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self.__height = new_height
        else:
            print("Height must be greater than 0.")

    # ----- extra behavior -----
    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


if __name__ == "__main__":
    rectangle = Rectangle(3, 4)

    print("Width:", rectangle.width)       # getter, no parentheses
    print("Height:", rectangle.height)
    print("Area:", rectangle.area())

    rectangle.width = 10                   # setter, looks like assignment
    rectangle.height = 5
    print("\nAfter update")
    print("Width:", rectangle.width)
    print("Height:", rectangle.height)
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())

    print("\nInvalid update")
    rectangle.width = -7                   # rejected by validation
    print("Width is still:", rectangle.width)
