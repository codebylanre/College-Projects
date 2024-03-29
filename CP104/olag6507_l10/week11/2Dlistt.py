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

matrix = [(1, 2, 4), [6, 9, 7], [3, 8, 5]]
# print(matrix[1][2])

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()


i = 0
while i < len(matrix):
    print(matrix[i])
    i += 1
