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


count = 0
total = 0
for i in range(5):
    number = int(input(f"Enter number: "))
    count += 1
    total += number

print(f"There are a total of {count} numbers")
print("The total is:", total)
print("The average is:", total/count)


'''
count = 1
total = 0
for i in range(5):
    number = int(input(f"Enter {count} number: "))
    count += 1
    total += number

    if count:
        break
    
    
print(f"There are a total of {count} numbers")
print("The total is:", total)
print("The average is:", total/count)
'''
