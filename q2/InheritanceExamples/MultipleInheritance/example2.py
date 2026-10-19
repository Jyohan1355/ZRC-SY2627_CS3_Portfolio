class Parent1:
    def method1(self):
        return "Method from Parent1"

class Parent2:
    def method2(self):
        return "Method from Parent2"

class ChildClass(Parent1, Parent2):
    pass

# Creating an instance of ChildClass
child_obj = ChildClass()

# Accessing methods from parent classes
output1 = child_obj.method1()
output2 = child_obj.method2()

print(output1)  
print(output2) 
