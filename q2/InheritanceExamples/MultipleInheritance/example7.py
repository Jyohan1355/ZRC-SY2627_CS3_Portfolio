# Creating first parent class.
class Parent1:
    def method(self):
        return "Method from Parent1"

# Creating second parent class.
class Parent2:
    def method(self):
        return "Method from Parent2"

# Creating child class that inherits from both parent classes.
class ChildClass(Parent1, Parent2):
    def child_method(self):
        return "Method in ChildClass"

# Creating an instance of ChildClass
child_obj = ChildClass()

# Accessing methods from parent classes.
output1 = child_obj.method()  # This will call the method from Parent1
output2 = child_obj.child_method() # This will call the method from ChildClass.

print(output1)
print(output2)
