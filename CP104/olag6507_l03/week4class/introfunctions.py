"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-20"
-------------------------------------------------------
"""


def square1(number):
    sq = number*number
    print(f"The square of the number is {sq}")


def square2(number):
    sq = number*number
    return sq


square1(20)
sq = square2(10)
print(f"The square of the number is {sq}")
