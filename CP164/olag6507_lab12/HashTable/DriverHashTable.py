'''
Created on Jul. 24, 2023

@author: Zara
'''

from HashTable import HashTable
if __name__=='__main__':
    hashT = HashTable(20)
    hashT.add("good","eggs")
    hashT.add("better","ham")
    hashT.add("ad","spam")
    hashT.add("ga","do not collide")
    #hashT.add("good","cake")
    
    
    hashT.printAll()
    
