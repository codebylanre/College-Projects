"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-22"
-------------------------------------------------------
"""

from functions import day_of_week

day_num = int(input("Please enter a number between 1 and 7: "))

day = day_of_week(day_num)

print(f"day_of_week {day_num} = {day}")
