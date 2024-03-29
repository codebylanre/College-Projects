'''
Created on Aug 1, 2023

@author: abdulbasitolagunju
'''
def largest_total(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the total of the two largest values of
    val1, val2, and val3.
    Use: total = largest_total(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        total - the total of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    first_large = 0
    second_large = 0
    
    if val1 > val2:
        first_large = val1
        if val2 > val3:
            second_large = val2
        else:
            second_large = val3
            
    if val2 > val1:
        first_large = val2
        if val1 > val3:
            second_large = val1
        else:
            second_large = val3
            
    return first_large + second_large

print(largest_total(-8,12,20))