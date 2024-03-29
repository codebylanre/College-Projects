"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@mylaurier.ca
__updated__ = "Sep 23, 2023"
------------------------------------------------------------------------
"""

from Book import Book
from booklibrary import Library

def test_books():
    print("Testing Book")
    book1 = Book("Adventures of Huckleberry Finn", "Mark Twain", 1884, "Page 1 content\nPage 2 content", "$ 20")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Chapter 1 content\nChapter 2 content", "$ 21")
    book3 = Book("Harry Porter", "J. K. Rowling", 1949, "Part 1 content\nPart 2 content", "$ 25")
    book4 = Book("Marvel", "Stan lee", 1940, "Chapter I content\nChapter II content", "$ 21")
    book5 = Book("DC", "Stan Lee", 1813, "Chapter 1 content\nChapter 2 content", "$ 16")

    print(book1)
    print(book2)
    print(book3)
    print(book4)
    print(book5)
    
def test_library():
    print("Testing book library")
    library = Library(5)  # Library capacity 5 books
    
    # Creating Library book objects
    book1 = Book("Title 1", "Author 1", 2000, "Content 1", 10)
    book2 = Book("Title 2", "Author 2", 2005, "Content 2", 12)
    book3 = Book("Title 3", "Author 3", 2010, "Content 3", 14)
    book4 = Book("Title 4", "Author 4", 2015, "Content 4", 16)
    book5 = Book("Title 5", "Author 5", 2020, "Content 5", 18)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
    
    # Display details of books in library
    library.display_books()
    

if __name__ == "__main__":
    test_books()
    print()  # For fine printing and spacing to distinguish next function
    test_library()
