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

def get_substring_positions(string1, string2):
    
    count = 0
    strings = []

    for i in range(len(string1) - 1):
        
        # Extracing string of two characters from both arguments
        sub1 = string1[i:i+2]
        sub2 = string2[i:i+2]

        if sub1 == sub2:
            strings.append(sub1) # To append the commnon values to a list 
        
            count += 1
    print(strings)
    return count

print(get_substring_positions("hello", "yello"))
print()
print(get_substring_positions("dobatz","docatzz"))

