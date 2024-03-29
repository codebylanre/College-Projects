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


from CircularLinkedList import CircularLinkedlist

if __name__=='__main__':
    
    mylist = CircularLinkedlist()
    
    # Testing the add function
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)   

    
    

    # Implmenting the find method
    print(mylist.find(17))
    print()
    
    # Implementing the __str__ speecial method
    print(mylist)

    # Implementing the remove method
    mylist.remove(77)

    print('------------------------------')
    # Implmenting the __str__ after a removal
    print(mylist)

    print()
    # Implementing isempty method
    print(mylist.isEmpty())
    
    print()
    # Implementing the find(index) method after removal
    print(mylist.find(17))

    




    
