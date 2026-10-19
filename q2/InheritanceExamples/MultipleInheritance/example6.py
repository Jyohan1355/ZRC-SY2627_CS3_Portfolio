# Parent class 1.
class Pan_card:
  # Constructor method of parent class 1.
    def __init__(self):
        self.pan_number = "PAN029192AB"
        print("This is a Pan_card class")

# Parent class 2.
class Aadhar_card:
    def __init__(self):
        self.aadhar_number = "456789720013423"
        print("This is a aadhar_card class")

# Child class.
class Bank_account_opening(Pan_card, Aadhar_card):
  # Constructor method of child class.
    def __init__(self):
      # Calling constructor of parent class 1 using super() function.
        super().__init__()
      # Calling constructor of parent class 2 using class name.
        Aadhar_card.__init__(self)
        print("This is a bank_account_opening class")

  # Method of child class.
    def customer_info(self):
        print("Pen_number: ", self.pan_number)
        print("Aadhar_number: ", self.aadhar_number)

# Creating an instance of derived class.
bank_obj = Bank_account_opening()

# Calling methods of derived class.
bank_obj.customer_info()
