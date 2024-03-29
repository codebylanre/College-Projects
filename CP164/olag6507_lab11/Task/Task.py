"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Nov 26, 2023"
------------------------------------------------------------------------
"""




from Heap import MaxHeap
from ArrayStack import ArrayStack



def heapsort():
    print("Task 1")
    stack = ArrayStack()


    # Create instance
    heapobject = MaxHeap(12)

    # Add to heap
    heapobject.insert(75)
    heapobject.insert(68)
    heapobject.insert(89)
    heapobject.insert(59)
    heapobject.insert(65)
    heapobject.insert(48)
    heapobject.insert(12)
    heapobject.insert(44)
    heapobject.insert(37)
    heapobject.insert(24)
    heapobject.insert(52)
    heapobject.insert(20)
    heapobject.update(48, 77)
    

    # Remove from heap
                                                                           
    
    while len(heapobject) != 0:
         
        result = heapobject.remove()
        stack.push(result)
        # heapobject._siftDown(0)  # Restore the heap property
        # heapobject._siftUp(0)

    stack.printStack()





heapsort()


