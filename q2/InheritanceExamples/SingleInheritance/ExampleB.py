# Parent class
class Vehicle:
  # Parent class constructor.
    def __init__(self, brand):
        self.brand = brand # instance variable.
  
  # Parent class method.
    def start_engine(self):
        return f"{self.brand} engine started"

# Derived class.
class Car(Vehicle):
  # Derived class constructor.
    def __init__(self, brand, model):
      # Calling constructor of parent class using super() function.    
        super().__init__(brand)
        self.model = model # instance variable.
  
  # Overriding parent class method with specific implementation inside derived class. 
    def start_engine(self):
        return f"{self.brand} {self.model} car's engine started"

# Creating an instance of the child class
car = Car("Toyota", "Camry")

# Calling overridden methods.
print(car.start_engine())
