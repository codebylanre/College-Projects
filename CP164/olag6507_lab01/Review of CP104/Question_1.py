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

def near_and_far(a, b, c):

    # Check if b is close to a.
    if abs(b - a) <= 1:

        # Check if c is far from a and b.
        if abs(c - a) >= 2 and abs(c - b) >= 2:
      
            result =  True
    
    # Check if c is close to a.
    elif abs(c - a) <= 1:

        # Check if b is far from a and c.
        if abs(b - a) >= 2 and abs(b - c) >= 2:
      
            result = True
    
    result = False

    return result

print(near_and_far(1, 1, 2))