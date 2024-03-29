"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-19"
-------------------------------------------------------
"""
# OPEN


def count_zeros(matrix):
    zero_count = 0
    for row in matrix:
        zero_count += row.count(0)
    return zero_count


# Test the function with a 2D list
matrix = [
    [0, 1, 0],
    [2, 0, 3],
    [0, 4, 0],
    [0, 0, 0]
]

result = count_zeros(matrix)
print("Number of zeros in the matrix:", result)

# GOG


def count_numbers(matrix):
    count = 0
    for row in matrix:
        for item in row:
            if item == 0:
                count += 1
    return count


def max_number(matrix):
    count = 0
    for row in matrix:
        for item in row:
            if item > max_num:
                max_num = item
    return max_num
