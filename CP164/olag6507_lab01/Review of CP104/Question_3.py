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

def sumDigits(n):
    # THIS WORkS WITH ONLY 3 DIGIT NUMBER
    hundredth = n // 100
    tenth = (n % 100) // 10
    unit = (n % 10)
    
    return hundredth + tenth +  unit

print(sumDigits(777))