"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-09-14"
-------------------------------------------------------
"""

def sum_without_twenties(a, b, c):
    if a in range(20, 30):
        a = 0
    if b in range(20,30):
        b = 0
    if c in range(20,30):
        c = 0
    
    return a + b + c

        
    
print(sum_without_twenties(21, 10, 23))