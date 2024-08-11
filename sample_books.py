# sample_books.py

from book import Book

def get_sample_books():
    return [
        Book("978-0135166307", "Effective Python", "Brett Slatkin", 2015),
        Book("978-0132350884", "Clean Code", "Robert C. Martin", 2008),
        Book("978-0262033848", "Introduction to Algorithms", "Thomas H. Cormen", 2009),
    ]
