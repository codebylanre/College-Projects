"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-05-29"
-------------------------------------------------------
"""

total_seconds = int(input("Enter number of seconds: "))

hours = total_seconds // 3600
seconds = total_seconds % 3600
minutes = seconds // 60
seconds = seconds % 60

print(
    f"There are {hours} hours, {minutes} minutes, and {seconds} seconds in {total_seconds} seconds")

# here are 1 hour, 1 minutes, and 21 seconds in 3681 seconds
