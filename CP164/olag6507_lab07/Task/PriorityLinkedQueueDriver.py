"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Oct 26, 2023"
------------------------------------------------------------------------
"""
from PriorityLinkedQueue import PriorityLinkedQueue


if __name__ == "__main__":
    PQ = PriorityLinkedQueue()

    PQ.enqueue("Item1", 1)
    PQ.enqueue("Item6", 2)
    PQ.enqueue("Item5", 3)
    PQ.enqueue("Item7", 2)
    PQ.enqueue("Item9", 4)

    while PQ:
        print(PQ.dequeue())