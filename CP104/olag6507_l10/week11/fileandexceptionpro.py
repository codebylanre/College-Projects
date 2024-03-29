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
except Exception as ex:
    print(ex)
    # ex is just a variable and different values can be used in terms of ex
