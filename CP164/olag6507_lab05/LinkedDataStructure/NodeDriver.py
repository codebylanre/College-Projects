'''
Created on May 27, 2023

@author: Zara

'''
from SinglyLinkedList import SinglyLinkedList

if __name__=='__main__':
    
    mylist = SinglyLinkedList()
    
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)   
    mylist.modified_add(93,33)
    
    

    print(mylist.get_second_to_last_node())
    print(mylist.get_max()) 
    print(mylist.search(17))
    
    mylist.display()
    # mylist.remove(31)
    print('\n-------------------------')
    mylist.display()


