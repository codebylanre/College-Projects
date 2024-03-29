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

from functions import mow_lawn

width = float(input("Enter width of lawn in metres: "))
length = float(input("Enter length of lawn in  metres: "))
speed = float(input("Enter speed of lawn in m² per minute: "))

time_minutes = mow_lawn(width, length, speed)


print(f"mow_lawn({width}, {length}, {speed}) = {time_minutes}")
