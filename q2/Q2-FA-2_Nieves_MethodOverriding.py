class Patient:
    def __init__(self, name, bill_amount):
         self.name = name
         self.bill_amount = bill_amount

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_bill_amount(self):
        return self.bill_amount

    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount

    def calculate_bill(self):
        return self.bill_amount

class SeniorPatient(Patient):
    def __init__(self, name, bill_amount, discount):
        super().__init__(name, bill_amount)
        self.discount = discount

    def calculate_bill(self):
        discounted_amount = self.bill_amount * (1 - self.discount)
        return discounted_amount

class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount, philhealth_coverage):
        super().__init__(name, bill_amount)
        self.philhealth_coverage = philhealth_coverage

    def calculate_bill(self):
        covered_amount = self.bill_amount * (1 - self.philhealth_coverage)
        return covered_amount

patient1 = Patient("Jerolf E. Matas", 1000)
senior_patient1 = SeniorPatient("Mark Jason L. Saratao", 1000, 0.2)
philhealth_patient1 = PhilHealthPatient("Karl Vincent Ballares", 1000, 0.5)

print(f"Patient: {patient1.get_name()}, Bill Amount: {patient1.calculate_bill()}")
print(f"Senior Patient: {senior_patient1.get_name()}, Bill Amount after Discount: {senior_patient1.calculate_bill()}")
print(f"PhilHealth Patient: {philhealth_patient1.get_name()}, Bill Amount after PhilHealth Coverage: {philhealth_patient1.calculate_bill()}")
