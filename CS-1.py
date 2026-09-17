class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


class Student:
    def __init__(self, name):
        self.name = name


# Create a course
course = Course("Computer Science")

# Create students
student1 = Student("Juan")
student2 = Student("Maria")

# Add students to the course
course.add_student(student1)
course.add_student(student2)