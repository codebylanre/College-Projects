"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-03"
-------------------------------------------------------
"""


def compound_interest():
    p = float(input("Enter your Principal amount:"))
    rate = float(input("Enter your annual rate:"))
    time = int(input("Enter the duration of deposit/borrow:"))
    compound = int(input("Enter compound interest:"))
    return p, time, rate, compound


p, time, rate, compound = compound_interest()
w = rate/100

amount = p * (1 + (w/compound))**(compound*time)

print(f"Balance: ${amount:.10f}")
