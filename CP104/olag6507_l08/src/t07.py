"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-03"
-------------------------------------------------------
"""
from functions import list_categorize

# values = [1, -2, 0, 3, -4, 5, 0]

negatives, positives, zeroes, evens, odds = list_categorize(
    [94, 96, -22, -79, -28, -26, -50, 71, 24, -32, 0])

print(negatives, positives, zeroes, evens, odds)
