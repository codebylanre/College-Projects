'''
Created on Jun. 18, 2023

@author: Zara
'''
from Node import Node
class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""
    def __init__(self):
        """Create an empty queue."""
        self.head = None
        self.tail = None
        self.size = 0 # number of queue elements
    
    def len (self):
        """Return the number of elements in the queue."""
        return f'Length: {self.size}'
    
    def is_empty(self):
        """Return True if the queue is empty."""
        return self.size == 0
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty( ):
            raise Exception( "Queue is empty" )
        return self.head.data # front aligned with head of list
    
    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty."""
        if self.is_empty( ):
            raise Exception( "Queue is empty" )
        answer = self.head.data

        #insert code here
        self.head = self.head.next
        self.size -= 1
        
        if self.is_empty(): # Special case for empty queue
            self.tail = None # Removed head had been the tail
        return answer
        
    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = Node(e) # node will be new tail node
        if self.is_empty( ):
            #insert code here # special case: previously empty
            self.head = newest 
        else:
            #insert code here
            self.tail.next = newest
        self.tail = newest
        #insert code here # update reference to tail node
        self.size += 1
        
        
        
        
        
        
        
        
        
        