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

from PriorityNode import PriorityNode

class PriorityLinkedQueue:
    def __init__(self):
        """Create an empty queue."""
        self.head = None
        self.tail = None
        self.size = 0 

    def __len__(self):
        """Return the number of elements in the queue."""
        return self.size
    
    def is_Empty(self):
        """Return True if the queue is empty."""
        return self.size == 0
    
    def enqueue(self, item, priority):
        newest = PriorityNode(item, priority)

        # If the queue is empty, set the head and tail to the new node.
        if self.is_Empty():
            self.head = newest
            self.tail = newest
        
        # insert the new node at the end of the queue.
        else:
            self.tail.set_next(newest)
            self.tail = newest

        # Increment size od queue
        self.size += 1

    def dequeue(self):
        if self.is_Empty():
            return "Queue is empty"

         # remove the node with the highest priority from the queue.
        current_node = self.head
        previous_node = None
        while current_node.get_next() and current_node.get_next().priority >= current_node.priority:
            current_node = current_node.get_next()

        # If the current node is the head of the queue, set the head to the next node.
        if current_node == self.head:
            self.head = current_node.get_next()

        # remove the current node from the queue.
        else:
            previous_node = self.head
            while previous_node.get_next() != current_node:
                previous_node = previous_node.get_next()

            previous_node.set_next(current_node.get_next())

        # If the current node is the tail of the queue, set the tail to the previous node.
        if current_node == self.tail:
            self.tail = previous_node

        # reduce the size of queue and return the data of the dequeued node.
        self.size -= 1
        return current_node.get_data()
