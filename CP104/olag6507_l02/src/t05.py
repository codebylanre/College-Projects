"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      020688702
Email:   olag6507@mylaurier.ca
__updated__ = "2023-05-24"
-------------------------------------------------------
"""
# code to covert time

# inputs
total_seconds = int(input("Enter number of seconds: "))

# processing
hours = total_seconds // 3600
seconds = total_seconds % 3600
minutes = seconds // 60
seconds = seconds % 60

# output
print(f"The time is {hours}:{minutes}:{seconds}")


# to confirm this code
