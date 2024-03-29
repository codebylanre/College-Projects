"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-17"
-------------------------------------------------------
"""
from functions import count_frequency_value

fh = open("/Users/abdulbasitolagunju/school/CP104/olag6507_l10/src/numbers.txt", "r")
count = count_frequency_value(fh, 2)
print(f"2 appears {count} times in the file.")
fh.close()
