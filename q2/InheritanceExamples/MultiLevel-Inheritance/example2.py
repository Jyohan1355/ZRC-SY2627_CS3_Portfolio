# Define the top-level class GrandParent
class GrandParent(object):
  # Constructor for GrandParent class, takes a name parameter.
    def __init__(self, name):
        self.name = name  # Initialize the 'name' attribute

  # Method to get the name.
    def getName(self):
        return self.name

# Define the Parent class, which inherits from GrandParent.
class Parent(GrandParent):
  # Constructor for Parent class, takes name and age parameters.
    def __init__(self, name, age):
      # Call the constructor of the parent class (GrandParent)
        GrandParent.__init__(self, name)
        self.age = age  # Initialize the 'age' attribute

  # Method to get the age.
    def getAge(self):
        return self.age

# Define the Child class, which inherits from Parent.
class Child(Parent):
  # Constructor for Child class, takes name, age, emp_id, and salary parameters.
    def __init__(self, name, age, emp_id, salary):
      # Call the constructor of the immediate parent class (Parent)
        Parent.__init__(self, name, age)
        self.emp_id = emp_id  # Initialize the 'emp_id' attribute
        self.salary = salary  # Initialize the 'salary' attribute

  # Method to get the employee ID.
    def getEmp_Id(self):
        return self.emp_id

  # Method to get the salary.
    def getSalary(self):
        return self.salary

# Create an instance of the Child class by passing argument values.
child = Child("Mahikaa", 24, 23455, 90000)

# Print the name, age, employee id, and salary by calling methods on the 'child' object.
print(child.getName(), child.getAge(), child.getEmp_Id(), child.getSalary())
