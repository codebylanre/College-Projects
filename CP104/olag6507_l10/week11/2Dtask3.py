"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-24"
-------------------------------------------------------
"""
matrix = [(1, 2, 4), [6, 9, 7], [3, 8, 5]]
print("Using For Loop")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()


print("TRANSPOSE")
new_column = []
for i in range(len(matrix[0])):
    new_row = []
    for row in matrix:
        new_row.append(row[i])
    new_column.append(new_row)
# return new_column
