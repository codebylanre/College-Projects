"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Oct 14, 2023"
------------------------------------------------------------------------
"""
from Node import Node

class CircularLinkedlist:
    
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
            self.head.set_next(self.head)  # Point to itself to create a circular link
        else:
            current = self.head
            while current.get_next() != self.head:
                current = current.get_next()
            temp.set_next(self.head)
            current.set_next(temp)
            
    def remove(self, item):
        if self.head is None:
            return "Empty List"
        
        current = self.head
        previous = None
        found = False
        
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        
        if current == self.head:
            # If the item to remove is the head of the circular list
            last_node = self.head
            
            # Find the last node in the circular list
            while last_node.get_next() != self.head:
                last_node = last_node.get_next()
                
            if self.head == self.head.get_next():
                # If there is only one item in the list, remove it
                self.head = None  
            else:
                # Updaing the head to the next node in the list
                self.head = self.head.get_next()
            
            # Update the last node to point to the new head, this maintains the circular structure    
            last_node.set_next(self.head)
        else:
            # If not the head
            previous.set_next(current.get_next())
        return

        def remove(self, item):
            if self.head is None:
                return "Empty List"
            
            current = self.head
            previous = None
            found = False
            
            while not found:
                if current.get_data() == item:
                    found = True
                else:
                    previous = current
                    current = current.get_next()
            
            if previous == None:
                self.head = current.get_next()          # This method i previously made is flawed because the last item still points to the old self.head so i made a new method to correct it and didn't delete this so i can learn from this mistake in the future
            else:
                previous.set_next(current.get_next())
    
    def __str__(self):
        if self.head is None:
            return "List is Empty"
        
        current = self.head
        result = []
        
        while True:
            result.append(current.get_data())
            current = current.get_next()
            if current == self.head:
                break
            
        return " -> ".join(map(str, result))
            
    def __len__(self):
        if self.head is None:
            return 0
        
        current = self.head
        count = 0
        
        while current is not None:
            count += 1
            current = current.get_next()
            
        return count
    
    def isEmpty(self):
        result =  (self.head == None)
        return f"Is the list Empty? {result}"
            
    def find(self, item):
        current = self.head
        index = 0 
        found = False
        while not found:
            index += 1
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                
        return f"The index of {item} is: {index}"
                
                
                
        
        
        
        
        
        