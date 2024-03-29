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


class Book:
    def __init__(self, title, author, year, content, cost):
        self.title = title
        self.author = author
        self.year = year
        self.content = content
        self.cost = cost
        
    def __str__(self):
        return f"{self.title} by {self.author}"