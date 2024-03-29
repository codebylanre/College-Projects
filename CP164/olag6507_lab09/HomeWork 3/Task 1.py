"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Nov 14, 2023"
------------------------------------------------------------------------
"""

from Node import Node
from SinglyLinkedList import SinglyLinkedList

class LinkedList(SinglyLinkedList):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

def concatenate_lists(list1, list2):
    concatenated = LinkedList()

    # Append nodes from list1
    current = list1.head
    while current:
        concatenated.append(current.data)
        current = current.next  

    # Append list2
    current = list2.head
    while current:
        concatenated.append(current.data)
        current = current.next

    
    return concatenated



# Test code
L = LinkedList()
M = LinkedList()

for i in range(5):
    L.append(i)

for i in range(5,9):
    M.append(i)

print("Before concatenation")
print()
print("L")
L.display()
print()
print("M")
M.display()
print()

print("Concatenated list")
# Concatenate Test begins here
joinlinkedlist = concatenate_lists(L, M)

joinlinkedlist.display()





