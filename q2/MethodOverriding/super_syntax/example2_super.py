
class Publication:
    def display_info(self):
        print("Publication information")

class Book(Publication):
    def display_info(self):
        super().display_info()
        print("Additional book information")

book1 = Book()
book1.display_info()
