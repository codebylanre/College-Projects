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

import random
count0 = 0
count1 = 1
for i in range(1000):
    n = random.randint(0, 1)
    if n == 0:
        count0 += 1
    else:
        count1 += 1
print("Count of 0 is", count0)
print("Count of 1 is", count1)
