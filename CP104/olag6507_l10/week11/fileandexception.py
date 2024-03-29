"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-19"
-------------------------------------------------------
"""

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(num1/num2)
    open("xyz.txt", "r")
except ValueError:
    print("The input can not be converted to an int.")
except ZeroDivisionError:
    print("The denominator cannot be Zero.")
except FileNotFoundError:
    print("The file does not exist.")  
