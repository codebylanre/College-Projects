"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-09"
-------------------------------------------------------
"""

Date = int(input("Enter date in format MMDDYYYY: "))

month = Date // 1000000
day = (Date // 10000) % 100
year = Date % 10000
# print(year)
'''
# Extract the year
year = Date % 10000

# Extract day
Date = Date // 10000
day = Date % 100

# Extract month
month = Date//100
'''

# Output
print(f"The reformatted date is {year:4d}/{month:02d}/{day:02d}")
