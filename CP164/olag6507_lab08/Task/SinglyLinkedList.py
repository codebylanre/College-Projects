'''
Created on May 27, 2023

@author: Zara
'''

from Node import Node

class SinglyLinkedList:
    
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count
    
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found
    
    def remove(self, item): 
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
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            
    def display (self):
        current = self.head
        while current != None:
            print(current.get_data())
            current = current.get_next()
            
    def get_max(self):
        
        if self.head is None:
            return f"Empty list"
        
        max = self.head.data
        current = self.head
        
        while current != None:
            if current.data > max:
                max = current.data
                current = current.get_next()
            else:
                current = current.get_next()
        return f"The max value is: {max}"
    
    def get_second_to_last_node(self):
        if self.head is None:
            return f"Empty list"
        
        current = self.head
        while current.get_next().get_next() is not None:
            current = current.get_next()
            
        return current.get_data()
    
        def second_to_last(self):   # This works the same but i prefer the first one that i wrote
            current = self.head
            previous = None
        
            while current.get_next() != None:
                previous = current
                current = current.get_next()
                
            return previous.get_data()
    
    def modified_add(self, item1, item2):
        # Study this
        current = self.head
        found = False
        while not found:
            if current.get_data() == item1:
                found = True
            else:
                current = current.get_next()
                
        temp = Node(item2)
        temp.set_next(current.get_next())
        current.set_next(temp)
        
    def concatenate(self, other_list):
        if self.head is None:
            self.head = other_list.head
        else:
            current = self.head
            while current.next:
                pass
            # Incomplete code
            
            
            
    
    
    
    
        
  
            
            
        
        
        
        
        
        
                
