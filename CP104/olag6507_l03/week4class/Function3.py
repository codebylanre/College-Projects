"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-01"
-------------------------------------------------------
"""

CONVERSIONRATE = 0.6214


def kilometers_to_miles():
    distance_in_kilometers = float(input("Enter distance in kilometers:"))
    distance_in_miles = distance_in_kilometers*CONVERSIONRATE
    return distance_in_miles, distance_in_kilometers


distance_in_miles, distance_in_kilometers = kilometers_to_miles()

print(
    f"The conversion of {distance_in_kilometers:.2f} kilometers is {distance_in_miles:.2f} miles")
