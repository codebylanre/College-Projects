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
    newlist = []
    for words in list:
        if words in string:
            newlist.append(words)
    return newlist
