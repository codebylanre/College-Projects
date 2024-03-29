"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Oct 20, 2023"
------------------------------------------------------------------------
"""
from Queue1 import ParcelGameSimulation

game_driver = ParcelGameSimulation()

list_names = ['Abdulbasit', 'Kamilah', 'Steph', 'Bill', 'Jane', 'Brad', 'Tim']
constant = 7

result = game_driver.pass_the_parcel(list_names, constant)
print(result)
