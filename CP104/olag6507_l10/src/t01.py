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
from functions import customer_record

fh = open("customers.txt", "r")
result = customer_record(fh, 3)
print(result)
fh.close()
