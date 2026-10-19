# Python program to demonstrate multiple inheritance.
# Create first parent class.
class Parent1:
    def m1(self):
        print("m1 method of Parent1 class")

# Create second parent class.
class Parent2:
    def m2(self):
        print("m2 method of Parent2 class")

# Create a child class that inherits methods from both parent classes.
class ChildClass(Parent1, Parent2):
    def m3(self):
        print("m3 method of ChildClass class")

# Outside class definition.
# Create an object of ChildClass class.
child = ChildClass()

# Calling all the methods of child class using reference variable child.
child.m1()
child.m2()
child.m3()
