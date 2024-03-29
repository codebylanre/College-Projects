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
# WHILE LOOP
filename = "numbers.txt"
fh = open(filename, "r")

total = 0
count = 0

line = fh.readline()

while line != "":
    count += 1
    total += int(line)
    line = fh.readline()

print(f"The total is: {total}")
print(f"The average is: {total}/{count}")


# optimised while loop
filename = "numbers.txt"
fh = open(filename, "r")

total = 0
count = 0

line = fh.readline()

while line != "":
    line = line.strip()
    count += 1
    total += int(line)
    line = fh.readline()

print(f"The total is: {total}")
print(f"The average is: {total}/{count}")
# NOT REALLY OPTIMISED BUT THIS IS ALSO GOOD
filename = "numbers.txt"
total = 0
count = 0

with open(filename, "r") as fh:
    line = fh.readline().strip()
    while line:
        count += 1
        total += int(line)
        line = fh.readline().strip()

print(f"The total is: {total}")
print(f"The average is: {total}/{count}")


# FOR LOOP
filename = "numbers.txt"
fh = open(filename, "r")

total = 0
count = 0

for line in fh:
    count += 1
    total += int(line)

print(f"The total is: {total}")
print(f"The average is: {total}/{count}")

# OPTIMISED FOR LOOP
filename = "numbers.txt"
fh = open(filename, "r")

total = 0
count = 0

for line in fh:
    line = line.strip()
    if line:
        count += 1
        total += int(line)

print(f"The total is: {total}")
print(f"The average is: {total}/{count}")

# very optimised code
filename = "numbers.txt"

with open(filename, "r") as fh:
    numbers = [int(line.strip()) for line in fh if line.strip()]

count = len(numbers)
total = sum(numbers)
average = total/count

print(f"The total is: {total}")
print(f"The average is: {average}")


# TO OLDER ME PLEASE CHECK THE PRINT STATEMENTS OF THIS CODES AND VERIFY
# READ SCHOOL DOCS FOR FILE
