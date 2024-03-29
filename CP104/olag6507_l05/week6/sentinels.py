"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-16"
-------------------------------------------------------
"""

total = 0
count = 0

while True:
    score = int(input("Enter a test score (-1 to exit): "))
    if score == -1:
        break
    total += score
    count += 1

if count > 0:
    average = total / count
    print(f"Total: {total}")
    print(f"Count: {count}")
    print(f"Average: {average:.2f}")
else:
    print("No test scores were entered.")
