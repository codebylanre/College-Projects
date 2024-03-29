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
from SinglyLinkedList import SinglyLinkedList
from Node import Node

# Inherits all the methods of the Singlelinkedlist and then we can customise it the way we want for the add last method
class List(SinglyLinkedList):
    
    def sllist_addlast(self, data):
        "Add to the end of linkedlist"
        new_data = Node(data)

        if not self.head:
            # IF the list is empty
            self.head = new_data
        else:
            # Traverse to end of list
            current = self.head
            while current.next:
                current = current.next
            
            # Add the new node after last node
            current.next = new_data

        # update the size tracker
        self.size += 1


# TEST CODE
testList = List()
testList.sllist_addlast(1)
testList.sllist_addlast(2)
testList.sllist_addlast(3)
testList.sllist_addlast(4)

print("Linked list after adding elements")
testList.display()