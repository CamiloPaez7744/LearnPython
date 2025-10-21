# PascalCase
class Book:
    # Constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not checked out.")

first_book = Book("1984", "George Orwell")
second_book = Book("100 Years of Solitude", "Gabriel Garcia Marquez")

print(first_book.title)
print(second_book.author)

first_book.check_out()
first_book.check_out()
first_book.return_book()
second_book.check_out()