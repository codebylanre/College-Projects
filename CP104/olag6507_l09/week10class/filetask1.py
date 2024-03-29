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
filename = "sales.txt"

num_of_days = int(input("Enter number of days: "))
with open(filename, "w") as fh:

    for day in range(1, num_of_days+1):
        sales = float(input(f"Enter sales for day {day}: "))
        fh.write(f"Day {day}: {sales}\n")
