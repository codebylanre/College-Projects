'''
Created on Jul. 9, 2023

@author: Zara
'''
from BinarySearchTree import BinarySearchTree

if __name__=="__main__":
    theTree = BinarySearchTree()
    theTree.insert("Don",  "1974 1")
    theTree.insert("Herb", "1975 2")
    theTree.insert("Ken",  "1979 1")
    theTree.insert("Ivan", "1988 1")
    theTree.insert("Raj",  "1994 1")
    theTree.insert("Amir", "1996 1")
    theTree.insert("Adi",  "2002 3")
    theTree.insert("Ron",  "2002 3")
    theTree.insert("Fran", "2006 1")
    theTree.insert("Vint", "2006 2")
   
    

    
    # print(theTree.search("zara"))
    
    theTree.print()
    
    #theTree.delete("Raj")
    #theTree.print()

    # BINARY TASK TESTS STARTS HERE

    print()
