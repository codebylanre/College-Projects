'''
Created on Jul. 16, 2023

@author: Zara
'''
from Heap import MaxHeap

if __name__=="__main__":
    heapobject = MaxHeap(10)
    heapobject.insert(60)
    heapobject.insert(35)
    heapobject.insert(15)
    heapobject.insert(46)
    
    print(heapobject.__len__())
    print(heapobject.remove())
    print(heapobject.remove())
    
    
    
