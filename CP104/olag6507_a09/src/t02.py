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
from functions import file_integers
with open('numbers.txt', 'r') as file_handle:
    number_list = file_integers(file_handle)
    print(number_list)

file_handle.close()
