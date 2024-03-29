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

n = float(input("Enter the first number: "))

y = float(input("Enter the Second number: "))


operation = input(
    "Enter the operation to be performed ('a' for addition, 's' for subtraction, 'm' for multiplication, 'd' for division):  ")

if operation == "a":
    result = print(f"The answer is {n + y}")

elif operation == "s":
    result = print(f"The answer is {n - y}")
elif operation == "m":
    result = print(f"The answer is {n* y}")
else:
    operation == "d"
    result = print(f"The answer is {n/y}")
