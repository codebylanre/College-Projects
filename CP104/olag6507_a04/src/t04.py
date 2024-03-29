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

from functions import colour_blend

first = input("First colour: ")
second = input("Second colour: ")


rgb_colour = colour_blend(first, second)

print(f"Colour_blend({first},{second}) = {rgb_colour}")
