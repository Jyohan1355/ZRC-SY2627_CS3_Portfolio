# Parent class 1.
class Student:
  # Constructor method of parent class 1.
    def __init__(self):
        self.name = input("Enter the student name: ")
        self.rollNo = int(input("Enter your roll no: "))

  # Method of parent class 1.
    def display(self):
        print("\nName: ", self.name)
        print("Roll no: ", self.rollNo)

# Parent class 2.
class Marks:
    def __init__(self):
        self.p = int(input("Enter marks of physics: "))
        self.c = int(input("Enter marks of chemistry: "))
        self.m = int(input("Enter marks of maths: "))

  # Method of parent class 2.
    def display_marks(self):
        print("Marks of physics: ", self.p)
        print("Marks of chemistry: ", self.c)
        print("Marks of maths: ", self.m)

# Child class.
class Result(Student, Marks):
  # Constructor method of child class.
    def __init__(self):
        Student.__init__(self)
        Marks.__init__(self)
        self.total_marks = self.p + self.c + self.m
        self.per = self.total_marks * 100 / 300

  # Method of child class.
    def display_result(self):
        print("Total marks: ", self.total_marks)
        print("Percentage: ", self.per)

# Creating an instance of derived class.
obj = Result()

# Calling methods of derived class.
obj.display()
obj.display_marks()
obj.display_result()
