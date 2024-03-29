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
# while loop
filename = input("Enter the file name: ")
sport_name = input("Enter the sport name to look for: ")

fh = open(filename, "r")

sport = fh.readline()
while sport != "" and sport.strip() != sport_name:
    sport = fh.readline()

# See why loop stopped - end of file or sport names match?
if sport == "":
    print(f"{sport_name} not found in the file")
else:
    print(f"{sport_name} found in the file")

fh.close()

# USINGFORLOOP
filename = input("Enter the file name: ")
sport_name = input("Enter the sport name to look for: ")

fh = open(filename, "r")

found = False
for sport in fh:
    if sport.strip() == sport_name:
        found = True
        break

if found:
    print(f"{sport_name} found in the file")
else:
    print(f"{sport_name} not found in the file")

fh.close()
