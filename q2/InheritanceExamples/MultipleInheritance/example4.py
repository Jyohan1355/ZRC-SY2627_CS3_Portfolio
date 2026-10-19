# Creating first parent class.
class Parent1:
    def method(self):
        return "Method from Parent1"

# Creating second parent class.
class Parent2:
    def method(self):
        return "Method from Parent2"

# Creating a child class that inherits from both parent classes.
class ChildClass(Parent1, Parent2):
    def child_method(self):
      # Calling methods from both parent classes using super() function.  
        parent1_output = super().method()
        parent2_output = super().method()
        return f"ChildClass: {parent1_output} and {parent2_output}"

# Creating an instance of ChildClass
child_obj = ChildClass()

# Accessing method of ChildClass class. 
output = child_obj.child_method()
print(output)
