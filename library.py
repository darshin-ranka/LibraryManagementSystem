# library.py

from book import Book

class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}  # ISBN as key, Book object as value

    def add_book(self, book):
        if book.isbn in self.books:
            print(f"Book with ISBN {book.isbn} already exists in the library.")
        else:
            self.books[book.isbn] = book
            print(f"Book '{book.title}' added to the library.")

  
def borrow_book(self, user, isbn):
        if isbn in self.books:
            book = self.books[isbn]
            if book.is_available:
                book.is_available = False
                print(f"{user} has borrowed '{book.title}'.")
            else:
                print(f"The book '{book.title}' is currently borrowed by another user.")
        else:
            print(f"No book with ISBN {isbn} found in the library.")


    def return_book(self, isbn):
        if isbn in self.books:
            book = self.books[isbn]
            if not book.is_available:
                book.is_available = True
                print(f"The book '{book.title}' has been returned to the library.")
            else:
                print(f"The book '{book.title}' was not borrowed.")
        else:
            print(f"No book with ISBN {isbn} found in the library.")
