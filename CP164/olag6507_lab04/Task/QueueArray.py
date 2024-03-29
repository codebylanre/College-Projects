'''
Created on May 22, 2023

@author: Zara
'''
class QueueArray:
    def __init__(self, size): # Constructor
        self.__maxSize = size # Size of [circular] array
        self.__que = [None] * size # Queue stored as a list
        self.__front = 1 # Empty Queue has front 1
        self.__rear = 0 # after rear and 
        self.__nItems = 0 # No items in queue 
        
    def insert(self, item): # Insert item at rear of queue
        if self.isFull(): # if not full
            raise Exception("Queue overflow")
        self.__rear += 1 # Rear moves one to the right
        if self.__rear == self.__maxSize: # Wrap around circular array
            self.__rear = 0
        self.__que[self.__rear] = item # Store item at rear
        self.__nItems += 1
        return True
    
    def remove(self): # Remove front item of queue 
        if self.isEmpty(): # and return it, if not empty
            raise Exception("Queue underflow")
        front = self.__que[self.__front] # get the value at front 
        self.__que[self.__front] = None # Remove item reference 
        self.__front += 1 # front moves one to the right 
        if self.__front == self.__maxSize: # Wrap around circular arr.
            self.__front = 0 
        self.__nItems -= 1 
        return front 
    
    def peek(self): # Return frontmost item 
        return None if self.isEmpty() else self.__que[self.__front]
    
    def isEmpty(self): return self.__nItems == 0
    
    def isFull(self): return self.__nItems == self.__maxSize
    
    def __len__(self): return self.__nItems
    
    def __str__(self): # Convert queue to string
        if self.isEmpty():
            return "Queue is Empty"
        else:
            display = []
            index = self.__front
            for i in range(self.__nItems):
                display.append(str(self.__que[index]))
                index = (index + 1) % self.__maxSize
            return "\n".join(display)
        
    def empty_queue(self):
        if not self.__que:
            return "Queue is Empty" 
        # Iterate through the list and remove all elements
        while self.__que:
            self.__que.pop()
        return "Queue has been emptied"
        #
        # if self.__que.isEmpty():     
        #     return "Queue is Empty"
        # while not self.__que.isEmpty():
        #     for char in self.__que:
        #         char.pop()                   THIS IS NOT SMART, Make sure not to do this again
        # return "Queue has been emptied"
                       
                
                
                
                
                
                
                