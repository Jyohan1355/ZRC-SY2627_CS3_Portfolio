class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def speak(self):
        print(f"{self.name} makes a sound.")

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print(f"{self.name} is eating meat.")

    def speak(self):
        print(f"{self.name} roars.")

class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print(f"{self.name} is eating Leaves.")

    def speak(self):
        print(f"{self.name} trumpets.")

class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print(f"{self.name} is eating bananas.")

    def speak(self):
        print(f"{self.name} uhuhahah.")

print("Animal Class")
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("Cesar")
Animal = Animal("Secret animal")

Animal.eat()
Animal.speak()

lion.eat()
lion.speak()

elephant.eat()
elephant.speak()

monkey.eat()
monkey.speak()
