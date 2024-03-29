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
from functions import falling_time
distance = int(input("Enter fall distance in metres: "))

time = falling_time(distance)
print(f"Falling time after {distance}m is {time}")
