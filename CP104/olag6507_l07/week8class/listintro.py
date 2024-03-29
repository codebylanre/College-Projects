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

list1 = [1, 2, 3, 4, 5]
# print(list1)

tuple1 = (1, 2, 3, 4, 5)
# print(tuple1)

string1 = "12345"
# print(string1)

# for item in list1:
#     print(item)

# print(len(list1))
# for i in range(5):
#     print(list1[i])

for i in range(len(list1)):
    print(i)
# this would print the number of item in list counting from 0


for i in range(len(list1)):
    print(list1[i])
# this would print what the number represent
for i in range(len(list1)):
    print(i+1, list1[i])

i = 0
while i < len(list1):
    # print(i+1, list1[i])
    i += 1

list1 = list(range(1, 11))
# print(list1)
# print()


"""
COPYING LIST
"""

"""
1
"""
print(1)
# FOR LOOP METHOD
list1 = [1, 2, 3, 4, 5]
list2 = []
for item in list1:
    list2.append(item)


print(list1)
print(list2)

"""
2
"""
print()
print(2)
# CONCATENATION METHOD
list1 = [1, 2, 3, 4, 5]
list2 = [] + list1
print(list1)
print(list2)

"""
3
"""
print()
print(3)
# COPY METHOD
list1 = [1, 2, 3, 4, 5]
list2 = list1.copy()
list2[2] = 100
print(list1)
print(list2)
