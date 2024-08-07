'''
Created on Jun. 11, 2023

@author: Zara
'''

from Node import Node


class LinkedStack:
    def __init__(self):
        self.head= None  
        self.size=0
         
    def __len__ (self):
        """Return the number of elements in the stack."""
        return self.size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self.size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        temp = Node(e)
        if self.is_empty():
            #add your code here
            self.head = temp 
        else:
           #add your code here
           temp.set_next(self.head)
           self.head = temp
           
        self.size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty."""
        if self.is_empty( ):
            raise Exception( "Stack is empty" )
        
        return self.head.data               #top of stack is at head of list
    
    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Exception( "Stack is empty" )
    
        #add your code here 
        current = self.head
        answer = current.get_data()
        
        self.head = current.get_next() 
        self.size -= 1
           

        return answer
        
    def __str__(self):
        return self.head

    def max(self):
        """Return the maximum element from the stack"
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Exception( "Stack is empty" )
        
        current = self.head
        max = self.head.data
        
        while current is not None:
            if current.data > max:
                value = max
            else:
                current = current.get_next()
        
        return f"The maximum element is: {max}"
                
                # Troubleshoot this max method later
        def max_stack(self):
            """Return the maximum element from the stack"
            Raise Empty exception if the stack is empty."""
            if self.is_empty():
                raise Exception( "Stack is empty" )
            
            maximum = self.pop()
            
            while not self.is_empty():
                element = self.pop()
                
                if element > maximum:
                    maximum = element
            
            return maximum
                  
            def max_stacks(self):
                # Check if the stack is empty by calling s.is_empty(), if not continue
                maximum = self.pop()  # Initialize maximum with the top element
                
                while not self.is_empty():
                    if maximum < self.top():
                        maximum = self.pop()
                    else:
                        self.pop()
                return maximum
    def display (self):
        current = self.head
        while current != None:
            print(current.get_data())
            current = current.get_next()

    

    
    
    