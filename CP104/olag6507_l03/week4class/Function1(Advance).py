"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-05-31"
-------------------------------------------------------
"""

A_COST = 20
B_COST = 15
C_COST = 10


def calculate_income():
    tickets_a = int(input("Enter tickets sold for class A:"))
    tickets_b = int(input("Enter tickets sold for class B:"))
    tickets_c = int(input("Enter tickets sold for class C:"))
    income = tickets_a*A_COST + tickets_b*B_COST + tickets_c*C_COST
    return income


income = calculate_income()

print(f"The total income is {income}")
