"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-16"
-------------------------------------------------------
"""

n = int(input("Enter number of times to run: "))
for i in range(n):
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate (%): '))
    commission = sales*comm_rate / 100
    print(f'The commission is ${commission:,.2f}')
