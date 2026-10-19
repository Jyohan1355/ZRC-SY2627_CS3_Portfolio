# Python program to design a simple calculator using multiple inheritance.
class Addition:
    def add(self, x, y):
        return x + y

class Subtration:
    def sub(self, x, y):
        return x - y

class Multiplication:
    def multiply(self, x, y):
        return x * y

class Calculation(Addition, Subtration, Multiplication):
    def div(self, x, y):
        return x / y

# Create an instance of class Calculation.
cal = Calculation()

# Calling methods of parent classes as well as child class.
result1 = cal.add(20, 10)
result2 = cal.sub(40, 20)
result3 = cal.multiply(10, 30)
result4 = cal.div(20, 5)

print(result1)
print(result2)
print(result3)
print(result4)
