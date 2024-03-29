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

from functions import statistics

no_of_values = int(input("Enter number of values to calculate: "))

minimum, maximum, total, average = statistics(no_of_values)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Total:", total)
print("Average:", average)
