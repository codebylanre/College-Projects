"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-17"
-------------------------------------------------------
"""
from functions import number_stats
fh = open("numbers.txt", "r")
average, smallest, largest, total = number_stats(fh)
print("Smallest: ", smallest)
print("Largest: ", largest)
print("Total: ", total)
print("Average: ", average)
fh.close()
