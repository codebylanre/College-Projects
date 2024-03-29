"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-08"
-------------------------------------------------------
"""

integer = int(input("Enter a positive two-digit integer "))


tens_digit = integer//10
digits = integer % 10
sum = tens_digit + digits

print(f"The sum of the digits of {integer} is {sum}")



# integer = int(input("Enter a positive three-digit integer "))

# hundred = integer//100
# tens_digit = (integer%100) // 10
# digits = integer % 10
# sum = tens_digit + digits + hundred

# print(f"The sum of the digits of {integer} is {sum}")
