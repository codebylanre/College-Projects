"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-29"
-------------------------------------------------------
"""

from functions import range_sum
start = int(input("Start value: "))
increment = int(input("Increment: "))
count = int(input("Enter number of values: "))

total = range_sum(start, increment, count)

print(f"{total}")
