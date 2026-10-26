
# Parent class
class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    # Getter methods
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    # Setter methods
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    # Display publication information
    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


# Child class: Book
class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.__number_of_pages = number_pages

    # Getter method
    def get_number_of_pages(self):
        return self.__number_of_pages

    # Setter method
    def set_number_of_pages(self, number_pages):
        self.__number_of_pages = number_pages

    # Override display_info()
    def display_info(self):
        super().display_info()
        print("Number of Pages:", self.__number_of_pages)


# Child class: Magazine
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = issue_number

    # Getter method
    def get_issue_number(self):
        return self.__issue_number

    # Setter method
    def set_issue_number(self, issue_number):
        self.__issue_number = issue_number

    # Override display_info()
    def display_info(self):
        super().display_info()
        print("Issue Number:", self.__issue_number)


# Create objects
book1 = Book("Introduction to Python", "John Smith", 350)
magazine1 = Magazine("Science Monthly", "Jane Doe", 25)


# Display book information
print("=== BOOK INFORMATION ===")
book1.display_info()

print()

# Display magazine information
print("=== MAGAZINE INFORMATION ===")
magazine1.display_info()




# =============

# 2. Access private attributes using getters
print("\n=== GETTER METHODS ===")
print("Book Title:", book1.get_title())
print("Book Author:", book1.get_author())
print("Book Pages:", book1.get_number_of_pages())

print("Magazine Title:", magazine1.get_title())
print("Magazine Author:", magazine1.get_author())
print("Magazine Issue:", magazine1.get_issue_number())


# 3. Update attributes using setters
book1.set_title("Advanced Python Programming")
book1.set_author("Michael Brown")
book1.set_number_of_pages(420)

magazine1.set_title("Science and Technology")
magazine1.set_author("Emily Davis")
magazine1.set_issue_number(26)


# 4. Display updated information
print("\n=== UPDATED BOOK INFORMATION ===")
book1.display_info()

print("\n=== UPDATED MAGAZINE INFORMATION ===")
magazine1.display_info()


# 5. Store objects in a list
publications = [book1, magazine1]


# 6. Demonstrate polymorphism
print("\n=== ALL PUBLICATIONS ===")
for publication in publications:
    publication.display_info()
    print("--------------------")
