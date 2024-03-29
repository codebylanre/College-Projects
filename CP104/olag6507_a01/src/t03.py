"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-01"
-------------------------------------------------------
"""


def inches_to_centimetres():
    length_in_inches = float(input("Enter your length in inches:"))
    lenght_in_centimetres = length_in_inches * 2.54
    return lenght_in_centimetres, length_in_inches


lenght_in_centimetres, length_in_inches = inches_to_centimetres()

print(f"length in cm {lenght_in_centimetres}")

#print(f"The conversion of {length_in_inches:.2f} inches is {lenght_in_centimetres:.2f} centimetres")
