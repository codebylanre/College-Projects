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


def time(string):
    words = string.split("/")
    first = words[0]
    second = words[1]
    third = words[2]
    print("day:", first)
    print("month:", second)
    print("year:", third)


time('20/5/20')
