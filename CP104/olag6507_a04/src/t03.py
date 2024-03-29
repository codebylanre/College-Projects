"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-23"
-------------------------------------------------------
"""
from functions import largest_total

val1 = float(input("Enter first value: "))
val2 = float(input("Enter second value: "))
val3 = float(input("Enter third value: "))

total = largest_total(val1, val2, val3)

print(f"Largest_total({val1},{val2},{val3}) = {total}")
