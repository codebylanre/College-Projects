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

from QueueArray import QueueArray

class Stack_Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, item):
        # Move into inbound stack
        self.inbound_stack.append(item)

    def dequeue(self):
        # If outbound is empty, move from inbound
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
                
        # If outbound is not empty
        if self.outbound_stack:
            return self.outbound_stack.pop()
        else:
            return "Inbound is Empty"  
        

