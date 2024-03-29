"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-03"
-------------------------------------------------------
"""

from functions import get_weekday_name

for i in range(1, 8):
    day_input = int(input("Enter a day (1-7): "))
    day = get_weekday_name(day_input)
    print(day)
    break
