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

from Deque3 import Deque

d = Deque()
print()
print()
print(d.is_empty())
print(d.display())
print()
d.add_rear(4)#
print(d.display())
print()
d.add_rear('dog')#
print(d.display())
print()
d.add_front('cat')#
print(d.display())
print()
d.add_front(True)#
print(d.display())
print()
print(d.size())#
print()
print(d.is_empty())#
print()
d.add_rear(8.4)#
print(d.display())
print()
print(d.remove_rear())#
print(d.display())
print()
print(d.remove_front())#
print(d.display())
print()