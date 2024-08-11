# library_system.py

from library import Library
from sample_books import get_sample_books  # Import sample book data

class LibrarySystem:
    def __init__(self):
        self.library = Library("Reader")

    def add_sample_books(self):
        sample_books = get_sample_books()
        for book in sample_books:
            self.library.add_book(book)

    def start(self):
        self.add_sample_books()
        while True:
            print(f"\nWelcome to the {self.library.name} Library. Choose an option:")
            print("1. Display available books")
            print("2. Borrow a book")
            print("3. Add a book")
            print("4. Return a book")
            print("5. Quit")

            user_choice = input("Enter your choice: ")

            if user_choice == '1':
                self.library.view_available_books()
            elif user_choice == '2':
                book_isbn = input("Enter the ISBN of the book you want to borrow: ")
                user_name = input("Enter your name: ")
                self.library.borrow_book(user_name, book_isbn)
            elif user_choice == '3':
                book_isbn = input("Enter the ISBN of the book: ")
                book_title = input("Enter the title of the book: ")
                book_author = input("Enter the author of the book: ")
                book_year = input("Enter the publication year of the book: ")
                new_book = Book(book_isbn, book_title, book_author, book_year)
                self.library.add_book(new_book)
            elif user_choice == '4':
                book_isbn = input("Enter the ISBN of the book you want to return: ")
                self.library.return_book(book_isbn)
            elif user_choice == '5':
                print("Exiting the library system. Goodbye!")
                break
            else:
                print("Invalid option. Please choose again.")


if __name__ == '__main__':
    library_system = LibrarySystem()
    library_system.start()
