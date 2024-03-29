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


def perform_operation():
    n = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    operation = input(
        "Enter the operation to be performed ('a' for addition, 's' for subtraction, 'm' for multiplication, 'd' for division): ")

    if operation == "a":
        result = n + y
        return result
    elif operation == "s":
        result = n - y
        return result
    elif operation == "m":
        result = n * y
        return result
    elif operation == "d":
        if y != 0:  # Check for division by zero
            result = n / y
            return result
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."


print(perform_operation())
