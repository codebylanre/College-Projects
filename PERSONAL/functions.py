'''
Created on Aug 1, 2023

@author: abdulbasitolagunju
'''
def factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    
    product = 1
    for i in range(1,number+1):
        product *= i
    return product
    
# print(factorial(7))
def calories_counted(per_min, minutes):
    """
    -------------------------------------------------------
    Calculates and returns the number of calories burnt.
    Use: calories_count = calories_counted(per_min, minutes):
    -------------------------------------------------------
    Parameters:
        number - number of calories(float)
    Returns:
        calories counted, minutes
    ------------------------------------------------------
    """
    
    for i in range(5,minutes+1,5):
        calories = per_min * i
        print(f"{i:2d}  {calories:.1f}")
    return
        
print(calories_counted(4.1, 20))