'''
Created on Nov. 25, 2023

@author: Abdulbasit 
'''


from MinHeap import MinHeap

if __name__=="__main__":
    heapobject = MinHeap(10)
    heapobject.insert(60)
    heapobject.insert(35)
    heapobject.insert(15)
    heapobject.insert(46)
    
    print(heapobject.__len__())
    print(heapobject.remove())
    print(heapobject.remove())
    
    
    
