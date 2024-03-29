"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Nov 15, 2023"
------------------------------------------------------------------------
"""
from Node import Node

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        "Add a new node to the circular Linked list"
        new_node = Node(data)

        if not self.head:
            # If empty
            self.head = new_node
            self.head.next = self.head
        else:
            # Transverse to last node
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next

            
            # Add the new node after last node and make it point back to the head
            current_node.next = new_node
            new_node.next = self.head

    def remove(self, data):
        "Remove node with data from the circ linkedlist"
        if not self.head:
            return "Empty list"  
        
        if self.head.data == data:
            # If the head is the node to be removed update head
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            if current_node == self.head:
                # If only one node in list, set head to None
                self.head = None
            else:
                # Otherwise, update the head and last node's next pointer
                self.head = self.head.next
                current_node.next = self.head
            return
        
        # search for node with given data
        prev_node = self.head
        current_node = self.head.next

        while current_node != self.head:
            if current_node.data == data:
                # Found the node, remove it by pointer updating
                prev_node.next = current_node.next
                return
            prev_node = current_node
            current_node = current_node.next
    
    def transverse(self):
        "Transverse and print element of circ linkedlist"
        if not self.head:
            return "Empty"
        
        current_node = self.head
        while True:
            print(current_node.data, end=" ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print()