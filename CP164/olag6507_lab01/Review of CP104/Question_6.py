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

def add_by_column(matrix):
    
    column_sums = []
    for column in range(len(matrix)):
        column_sum = 0
        for row in range(len(matrix)):
            column_sum += matrix[row][column]
            print(matrix[row][column], end=" ")
        column_sums.append(column_sum)
    return column_sums


# TO TEST THE FUNCTION
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = add_by_column(matrix)
print(result)