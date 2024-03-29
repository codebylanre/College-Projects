"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-10"
-------------------------------------------------------
"""

st = "David"
# By index with a while loop:
i = 0
n = len(st)

while i < n:
    # print(st[i])
    i = i + 1

# By index with a for loop:
for i in range(n):
    print(st[i])


# By value with a for loop:
st = "David"
for c in st:
    print(c)
