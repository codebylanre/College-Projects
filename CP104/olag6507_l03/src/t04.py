"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-05-29"
-------------------------------------------------------
"""

# input
number = float(input("Enter number: "))
percent = float(input("Enter percentage: "))
discount = number*(percent/100)

# process
print(f"A {percent} percent discount on {number} is {discount: .1f}")
