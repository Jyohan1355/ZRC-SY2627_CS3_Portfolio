# Define a class called Teacher.
class Teacher:
  # Constructor method with a parameter 'name'
    def __init__(self, name):
        self.name = name
  # Declare a method in the parent class.
    def showMe(self):
        print("Teacher name: ", self.name)

# Define a class named Student that inherits from Teacher.
class Student(Teacher):
  # Overriding the showMe() method of the parent class.
    def showMe(self):
        print("Student name: ", self.name)

# Outside the class definition.
# Creating an instance of Teacher class.
teach = Teacher("Deepak")
teach.showMe() # calling method of the Teacher class.

# Creating an instance of Student class
st = Student("Mahika")
st.showMe() # calling method of Student class. 
