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
from functions import customer_by_id

fh = open("customers.txt", "r")
print("Find Customer by id_number")
# result = customer_by_id(fh, 45432)
ID = customer_by_id(fh, (int(input("Enter an ID:"))))
print(ID)
# print(result)
fh.close()
