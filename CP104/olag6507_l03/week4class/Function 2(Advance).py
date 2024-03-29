"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-01"
-------------------------------------------------------
"""

CONVERSIONRATE = 12


def feet_to_inches():
    number_of_feet = float(input("Enter number of feets:"))
    # return number_of_feet
    inches = number_of_feet*CONVERSIONRATE
    return inches, number_of_feet


#number_of_feet = number_of_feet
inches, number_of_feet = feet_to_inches()

print(f"The conversion of {number_of_feet}feet is {inches} inches")
