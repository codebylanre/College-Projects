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

from functions import date_extract

date = int(input("Enter a date in the format DDMMYYYY: "))

result = date_extract(date)

print(f"date_extract{date} = {result}")
