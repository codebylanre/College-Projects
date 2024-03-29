"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-09-14"
-------------------------------------------------------
"""

def filter_words(filename, words_to_remove):

    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()

        # REmoving the unwanted words and creating new list
        filtered_words = [word for word in words if word not in words_to_remove ]

        return filtered_words
    

# Creating the file with all the given words to test the code
with open("/Users/abdulbasitolagunju/school/CP164/WEEK 1/Login_lab00/essay.txt", "w") as example:
    example.write("like happy like birthday yep summer is totally here lol happy summer")

# This is where the work begins, FUNCTION TESTING
filename = "/Users/abdulbasitolagunju/school/CP164/WEEK 1/Login_lab00/essay.txt"
words_to_remove = ['like', 'whatever', 'lol', 'yep', 'totally']
result = filter_words(filename, words_to_remove)

print(result)
print()

for text in result:
    print(text)
    print()

