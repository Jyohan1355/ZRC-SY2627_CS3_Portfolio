
class Publication:
    def get_type(self):
        print("This is a publication.")

class Book(Publication):
    def get_type(self):
        super().get_type()
        print("This is a book.")

book1 = Book()
book1.get_type()
