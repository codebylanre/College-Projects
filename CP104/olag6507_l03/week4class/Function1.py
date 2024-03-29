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


def calculate_income():
    tickets_a = int(input("Enter tickets sold for class A:"))
    tickets_b = int(input("Enter tickets sold for class B:"))
    tickets_c = int(input("Enter tickets sold for class C:"))
    income = tickets_a*20 + tickets_b*15 + tickets_c*10
    return income


income = calculate_income()

print(f"The total income is {income}")
