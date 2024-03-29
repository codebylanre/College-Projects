"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Oct 26, 2023"
------------------------------------------------------------------------
"""
from Node import Node

class CircularLinkedQueue:
    """FIFO queue implementation using a Circularlinked list for storage."""
  
    def __init__(self):
        """Create an empty queue."""
        self.head = None
        self.size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self.size
    
    def is_empty(self):
        """Return True if the queue is empty."""
        return self.size == 0
    
    def enqueue(self, item):
        """Add an element to the circularqueue."""
        newest = Node(item)
        if self.is_empty():
            newest.next = newest
            self.head = newest
        else: 
            newest.next = self.head.next
            self.head.next = newest
        self.size += 1
    
    def dequeue(self):
        """Add an element to the circularqueue."""
        if self.is_empty():
            return "Queue is empty"
        item = self.head.next.data
        if self.size == 1:
            self.head = None      # Remove the last item
        else: 
            self.head.next = self.head.next.next # Update head's next to skip the dequeued item
        self.size -= 1

        return item


