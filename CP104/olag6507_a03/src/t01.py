"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-16"
-------------------------------------------------------
"""

from functions import feet_to_acres

square_footage = float(input("Enter the number of square foot: "))
acres = feet_to_acres(square_footage)


print(f"feet_to_acres {square_footage}  = {acres}")
