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
from functions import student_info

with open('students.txt', 'r') as file_handle:
    # file_handle = 820000075, 820000000, 69.11111111111111
    l_id, h_id, avg = student_info(file_handle)

print(l_id, h_id, avg)
