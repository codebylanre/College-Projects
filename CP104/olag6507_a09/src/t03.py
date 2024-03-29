"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-27"
-------------------------------------------------------
"""
from functions import file_stats

with open('addresses.txt', 'r') as file_handle:
    ucount, lcount, dcount, wcount, rcount = file_stats(file_handle)
    print(ucount, lcount, dcount, wcount, rcount)
file_handle.close()
