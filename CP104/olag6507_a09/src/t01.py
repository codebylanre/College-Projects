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
from functions import file_head
with open('students.txt', 'r', encoding='utf-8') as file_handle:
    file_head(file_handle, 5)

file_handle.close()
