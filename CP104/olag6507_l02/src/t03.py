"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      020688702
Email:   olag6507@mylaurier.ca
__updated__ = "2023-05-24"
-------------------------------------------------------
"""

# input

item1 = float(input("Enter the price of the first item : "))
item2 = float(input("Enter the price of the second item : "))
item3 = float(input("Enter the price of the third item : "))
item4 = float(input("Enter the price of the fourth item : "))
item5 = float(input("Enter the price of the fifth item : "))

# processing
Subtotal = item1 + item2 + item3 + item4 + item5

Sales_tax = Subtotal * 0.07  # sales tax is 7 percentage


# output
print("Your Subtotal is:", Subtotal)
print("Your Sales_tax is:", Sales_tax)
print("Your total is: ", Subtotal + Sales_tax)
