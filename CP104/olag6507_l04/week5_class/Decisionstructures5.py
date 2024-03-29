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


# def main():
pennies = float(input("Enter number of pennies: "))
nickels = float(input("Enter number of nickels: "))
dimes = float(input("Enter number of dimes: "))
quarters = float(input("Enter number of quarters: "))
total = pennies + (nickels * 5) + (dimes * 10) + (quarters * 25)


if total == 100:
    print("Congratulation you've just won the game")
elif total > 100:
    print("The amount entered is more than a dollar, Pls try again")
else:
    print("The amount entered is less than a dollar, Pls try again")
