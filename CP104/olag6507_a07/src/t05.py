"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-13"
-------------------------------------------------------
"""
from functions import is_sorted
result, index = is_sorted([4, 7, 10])
print(result, index)  # Output: True, -1

result, index = is_sorted([3, 2, 1])
print(result, index)  # Output: False, 1
