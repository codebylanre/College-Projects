"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-05"
-------------------------------------------------------
"""


def main(string, list):
    for words in list:
        if words in string:
            print("True")
        else:
            print("False")
