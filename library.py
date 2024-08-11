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

  
