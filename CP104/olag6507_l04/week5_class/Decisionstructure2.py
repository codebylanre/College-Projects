"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-07"
-------------------------------------------------------
"""


# def main(length, width, length1, length2):
length = float(input("Enter length of first rectangle"))
width = float(input("Enter width of first rectangle"))
length2 = float(input("Enter length of second rectangle"))
width2 = float(input("Enter width of second rectangle"))
area_of_rect1 = length * width

area_of_rect2 = length2 * width2
if area_of_rect1 > area_of_rect2:
    print("The first rectangle has a bigger area")
else:
    print("The second rectangle has a bigger area")
