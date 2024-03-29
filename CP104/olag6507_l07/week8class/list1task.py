"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-02"
-------------------------------------------------------
"""

numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
valid_numbers = []

for num in numbers:
    if num >= 0 and num <= 100:
        valid_numbers.append(num)
total = sum(valid_numbers)
average = total/len(valid_numbers)
print(total)
print(average)
