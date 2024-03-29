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
from functions import number_lines

with open('wilde.txt', 'r') as fh_read:
    with open('wilde_numbered.txt', 'w') as fh_write:
        number_lines(fh_read, fh_write)
