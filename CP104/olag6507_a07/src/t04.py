"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-13"
-------------------------------------------------------
"""
from functions import subtract_lists

minuend = input("Enter numbers (separated by spaces): ").split()
minuend = [int(num) for num in minuend]

subtrahend = input("Enter subtrahend number (separated by spaces): ").split()
subtrahend = [int(num) for num in subtrahend]
print("minuend before:", minuend)
print(subtract_lists(minuend, subtrahend))


# print("minuend after:")
