"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-16"
-------------------------------------------------------
"""

from functions import fraction_product

# num1, den1, num2, den2, = fraction_product(1, 2, 3, 4)
num1 = int(input("Enter numerator 1: "))
den1 = int(input("Enter denominator 1: "))
num2 = int(input("Enter numerator 2: "))
den2 = int(input("Enter denominator 2: "))
num, den, product = fraction_product(1, 2, 3, 4)


print(
    f"fraction_product({num1}, {den1}, {num2}, {den2}) = {num}, {den}, {product}")
