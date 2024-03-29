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

from Stack_Queue2 import Stack_Queue

queue = Stack_Queue()

queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)


print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

