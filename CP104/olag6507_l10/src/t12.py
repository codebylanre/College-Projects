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
from functions import find_shortest

fh = open("/Users/abdulbasitolagunju/school/CP104/olag6507_l10/src/words.txt", "r")
print("file 'words.txt' open for reading'")
shortest_word = find_shortest(fh)
print(f"{shortest_word} is the first shortest word")
fh.close()
