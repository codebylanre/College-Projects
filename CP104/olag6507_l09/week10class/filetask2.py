"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-12"
-------------------------------------------------------
"""
# USING A WHILE LOOP
filename = "sales.txt"
fh = open(filename, "r")

line = fh.readline()
count = 0
while line != "":
    count += 1
    line = fh.readline()
    print(line)
print(f"There are {count} data items in the file")


# USING A FOR LOOP
filename = "sales.txt"
fh = open(filename, "r")
count = 0
for line in fh:
    count += 1
    print(line)
print(f"There are {count} data items in the file")
