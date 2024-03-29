'''
Created on Nov. 25, 2023

@author: Abdulbasit 
'''
from PriorityNode import Node


class PriorityQueue:
    def __init__(self):
        self.head = None

    
    def enqueue(self, data, priority):
        new_node = Node(data, priority)
        if not self.head or priority > self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and priority <= current.next.priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node


    def dequeue(self):
        if not self.head:
            print("Queue is empty")
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data
        
    
    def peek(self):
        if not self.head:
            print("Queue is Empty")
            return None
        else:
            return self.head.data
        
    
    def display(self):
        current = self.head
        while current:
            print(f"Data: {current.data}, Priority: {current.priority}")
            current = current.next