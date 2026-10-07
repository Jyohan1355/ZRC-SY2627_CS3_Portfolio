"""
Activity 1 - Access Modifiers (public, protected, private)
Each class declares the attribute inside __init__() using the correct modifier.
"""


# 1. username: displayed and accessed by anyone -> PUBLIC (no underscore)
class GameCharacter:
    def __init__(self, username):
        self.username = username


# 2. balance: must NOT be accessed directly outside the class -> PRIVATE (__)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance


# 3. engineCode: only within the class and its subclasses -> PROTECTED (_)
class Vehicle:
    def __init__(self, engineCode):
        self._engineCode = engineCode


# 4. schoolName: safe for everyone to view and modify -> PUBLIC (no underscore)
class Student:
    def __init__(self, schoolName):
        self.schoolName = schoolName


# 5. voterID: hidden for security reasons -> PRIVATE (__)
class VotingSystem:
    def __init__(self, voterID):
        self.__voterID = voterID


if __name__ == "__main__":
    g = GameCharacter("Zyra01")
    print("1. Public username:", g.username)

    b = BankAccount(500)
    try:
        print(b.__balance)
    except AttributeError:
        print("2. Private balance: cannot be accessed directly outside the class")

    v = Vehicle("ENG-123")
    print("3. Protected engineCode (convention only):", v._engineCode)

    s = Student("PSHS-EVC")
    s.schoolName = "PSHS-ZRC"
    print("4. Public schoolName, modified:", s.schoolName)

    vs = VotingSystem("V-0001")
    try:
        print(vs.__voterID)
    except AttributeError:
        print("5. Private voterID: cannot be accessed directly outside the class")
