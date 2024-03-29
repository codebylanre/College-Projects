"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-08"
-------------------------------------------------------
"""

balloons = int(input("Enter the number of balloons: "))
children = int(input("Enter the number of Children: "))

received = balloons // children
left = balloons % children

print(f"Balloons per child: {received}")
print(f"Balloons left over: {left}")
