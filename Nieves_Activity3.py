"""
Activity 3 - BankAccount class (Encapsulation)
- Private attributes: __account_number, __balance
- Public setter methods: set_account_number(), set_balance()
  (a negative balance is ignored and a warning is issued)
- Public getter methods using the @property decorator
"""


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = 0
        self.__balance = 0.0
        self.set_account_number(account_number)
        self.set_balance(balance)

    # ----- setters -----
    def set_account_number(self, account_number):
        if isinstance(account_number, int) and account_number > 0:
            self.__account_number = account_number
        else:
            print("The account number must be a positive integer.")

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = float(balance)
        else:
            print("The balance must not be a negative number.")

    # ----- getters (@property) -----
    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance


def display(account):
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {account.balance:.2f}")


if __name__ == "__main__":
    a1 = BankAccount(12345, 1000)

    print("Account 1")
    display(a1)

    print("\nUpdate balance to -100")
    a1.set_balance(-100)       # ignored, warning issued
    display(a1)

    print("\nUpdate balance to 2500.5")
    a1.set_balance(2500.5)
    display(a1)

    print("\nUpdate account number to 67890")
    a1.set_account_number(67890)
    display(a1)
