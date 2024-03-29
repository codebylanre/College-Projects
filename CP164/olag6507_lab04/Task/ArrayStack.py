'''
Created on May 14, 2023

@author: Zara Hamid
'''
class ArrayStack: 
    """ LIFO Stack implementation using Python list """

    def __init__(self):
        self.data = []
        
    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self.data)
        

    def  push(self, element): 
        """Add element e to the top of the stack"""
        self.data.append(element) 

    def  pop(self): 
        assert not self.isEmpty(),'Can not pop from an empty list'
        x = self.data.pop();
        return x
        # print('Last item has been poped from the list',x)

    def  printStack(self): 
        for i in self.data:
            print(i)

    def isEmpty(self):
        return(len(self.data) == 0)

    def peek(self):
        assert not self.isEmpty(),'Stack is Empty'
        print(self.data[len(self.data) - 1]) ;