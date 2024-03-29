'''
Created on Sep 22, 2023

@author: abdulbasitolagunju
'''

def factorial(n):
    assert n >= 0, "Factorial is only defined for non-negative integers"
    result = 1
    
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(-4))