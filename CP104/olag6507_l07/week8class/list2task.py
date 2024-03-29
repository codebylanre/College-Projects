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

valid_numbers = list(range(1, 501))
for num in valid_numbers:
    if num > 500:
        break
    elif num > 150:
        continue
    elif num % 5 == 0:
        print(num)
