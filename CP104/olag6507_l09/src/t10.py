"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-10"
-------------------------------------------------------
"""
from functions import text_analyze

uppr, lowr, dgts, whtspc = text_analyze('Python uses whitespace indentation, rather than curly brackets or keywords, to delimit blocks.')

print(uppr, lowr, dgts, whtspc)
