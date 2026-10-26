
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating.")

    def sleep(self):
        print(self.name, "is sleeping.")

    def make_sound(self):
        print(self.name, "makes a sound.")


# Child class: Dog overrides make_sound()
class Dog(Animal):
    def make_sound(self):
        print(self.name, "says Woof!")


# Child class: Cat overrides make_sound()
class Cat(Animal):
    def make_sound(self):
        print(self.name, "says Meow!")


# Create objects
animal1 = Animal("Generic Animal")
dog1 = Dog("Bruno")
cat1 = Cat("Kitty")


# Call the make_sound() method
animal1.make_sound()
dog1.make_sound()
cat1.make_sound()
