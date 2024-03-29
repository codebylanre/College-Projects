"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Oct 7, 2023"
------------------------------------------------------------------------
"""

from QueueArray import QueueArray

def QueueClient():
    queue = QueueArray(7)
    names = ["Akbar", "John", "Fatima", "Isaac", "Ibukun", "Chan", "Lily"]

    # Inserting names with for loop
    for name in names:
        queue.insert(name)
        
    print(queue)
    print(f"Is Queue full?, {queue.isFull()}")
    print()
   
    # Removing contents of Queue 
    print("Removing from Queue")
    while not queue.isEmpty():
        removed = queue.remove()
        print(f"Removed: {removed}")
    
QueueClient()