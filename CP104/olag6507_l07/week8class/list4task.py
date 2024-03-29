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
import random


lottery_numbers = []

# GENERATE NUM
for num in range(7):
    lottery_numbers.append(random.randint(0, 9))

# DISPLAY CONTENT
for value in lottery_numbers:
    print(value, end=" ")


