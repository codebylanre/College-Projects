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

from CircularLinkedQueue import CircularLinkedQueue

if __name__ == "__main__":

    CQ1 = CircularLinkedQueue()


    CQ1.enqueue(12)
    CQ1.enqueue(20)
    CQ1.enqueue(33)

    print(len(CQ1))

    print(CQ1.dequeue())