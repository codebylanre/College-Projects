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


def max_even_numbers(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)

    return max(even)


numbers = [1, 2, 3, 4, 57, 35, 26, 36, 2, 32, 234]
number = max_even_numbers(numbers)
print(number)
