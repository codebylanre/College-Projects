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

class  Library:
    def __init__(self, capacity = 10):
        """
        creates a library with a maximum capacity and an empty list of books.
        """
        self._books = [None] * capacity # reserves space just like scoreboard code
        self._n = 0  # Number of books (insights from scoreboard code)
        
    def __getitem__(self, k):
        return self._books[k] # Return index for book
    
    def __len__(self):
        return self._n
    
    def add_book(self, book):
        """
        add book to library
        """
        if self._n < len(self._books):
            self._books[self._n] = book
            self._n += 1
            
    def display_books(self):
        """
        Display the details of all books
        """
        for book in self._books[:self._n]:
            print(book)
            
            
            
            
    