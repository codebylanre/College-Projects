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

print("Using For Loop")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
# for apple in range(len(matrix)):
#     for banana in range(len(matrix[apple])):
#         print(matrix[apple][banana], end=" ")
#     print()


print("Using While Loop")
i = 0
while i < len(matrix):
    j = 0
    while j < len(matrix[i]):
        print(matrix[i][j], end=" ")
        j += 1
    i += 1
    print()
