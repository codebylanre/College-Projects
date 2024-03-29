"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-14"
-------------------------------------------------------
"""


def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 400 == 0:
        leap = True
    # Write your logic here

    return leap


year = int(input())
print(is_leap(year))
