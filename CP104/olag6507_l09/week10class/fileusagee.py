"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-13"
-------------------------------------------------------
"""
from os import path

filename = input("Enter file name: ")
if path.exists(filename):
    fh = open(filename, "r")
    # Process file
    ...
    fh.close()
else:
    print(f"File {filename} does not exist.")
