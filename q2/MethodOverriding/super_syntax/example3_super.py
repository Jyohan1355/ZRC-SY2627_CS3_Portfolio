
class Publication:
    def describe(self):
        print("A publication")

class Book(Publication):
    def describe(self):
        super().describe()
        print("A book")

class Textbook(Book):
    def describe(self):
        super().describe()
        print("A textbook")

textbook1 = Textbook()
textbook1.describe()
