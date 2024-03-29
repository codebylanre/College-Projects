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

from LinkedQueue import LinkedQueue
from Plant import Plant



def pythonlist_to_Queue(plant_obj, empty_queue):
    for plant in plant_obj:
        empty_queue.enqueue(plant)

    return empty_queue

def equals(queue1, queue2):
    if len(queue1) != len(queue2):
        return False
    while queue1:
        if queue1.dequeue() != queue2.dequeue():
            return False
    
    return True

def main():
    print("Testing Task 1")
    # Create series of plant objects
    plant_obj = [
        Plant("Rose", "Shrub", 30, "Moderate"),
        Plant("Tulip", "Wildflower", 15, "Low"),
        Plant("Maple", "Vine", 120, "High")
    ]

    empty_queue = LinkedQueue()
    result = pythonlist_to_Queue(plant_obj, empty_queue)
    while result:
        item = result.dequeue()
        print(item)
    
    print("Testing Task 2")
    queue1 = LinkedQueue()
    queue2 = LinkedQueue()
    for i in range(2, 10):
        queue1.enqueue(i)
    
    for i in range(4,9):
        queue2.enqueue(i)
    
    result = equals(queue1, queue2)
    print()
    print(result)


if __name__ == "__main__":
    main()