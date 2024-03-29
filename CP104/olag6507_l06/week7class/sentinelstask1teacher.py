"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-22"
-------------------------------------------------------
"""

score = int(input("Enter a test score (betwenn 0 and 100): "))

total = 0
count = 0
while score != -1:
    total += score
    count += 1
    score = int(
        input("Enter a test score (between 0 and 100, enter -1 to quit): "))

average = total/count
print(f"The total is {total}, the count is {count} and average is {average}")
