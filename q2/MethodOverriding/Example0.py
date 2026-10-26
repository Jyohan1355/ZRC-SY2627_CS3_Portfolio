
# Parent class
class Animal:
    def make_sound(self):
        print("Some sound.")

# Child class inherits from Animal
class Dog(Animal):
    pass

# Create objects
animal = Animal()
dog = Dog()

# Call the methods
animal.make_sound()
dog.make_sound()
