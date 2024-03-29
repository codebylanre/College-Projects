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

from functions import list_indexes

numbers = input("Enter numbers (separated by spaces): ").split()
numbers = [int(num) for num in numbers]

target_number = int(input("Enter target number: "))

indexes = list_indexes(numbers, target_number)
print("Indexes of target number:", indexes)


# from functions import list_indexes
#
# numbers = int(input("Enter numbers: "))
# target_number = int(input("Enter target number: "))
#
# numbers, target_number = list_indexes
#
# print(numbers, target_number)
