"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@mylaurier.ca
Section: CP164 Lab Fall 2023
__updated__ = "Oct 5, 2023"
------------------------------------------------------------------------
"""

from Plant import Plant
from QueueArray import QueueArray
from ArrayStack import ArrayStack


def pythonlist_to_Queue(list, queue): # Takes a list of string and an empty Queue argument
    print("Lab Task 1")
    for char in list:
        queue.insert(char)
    return queue

def equals(queue1, queue2):
    print("Lab Task 3")
    if len(queue1) != len(queue2):
        return False
    while not queue1.isEmpty():
        if queue1.remove() != queue2.remove():
            return False
    return True

def reverse_queue(queue):
    print("Lab Task 4")
    stack = ArrayStack()
    new_queue = QueueArray(20)

    while queue:
        stack.push(queue.remove())

    while not stack.isEmpty():    # I could also just say While stack but i wont to maintain the CP164 code structure
        new_queue.insert(stack.pop())

    return new_queue



 # Test code starts from here
def main():
    print("Testing List to Queue")
    list = ['hi', 'hello', 'Broom', 'Van']
    queue = QueueArray(10)
    pythonlist_to_Queue(list, queue)
    print(queue)
    print()
    
    print("Testing Empty queue")
    queue = QueueArray(10)
    names = ["Abdulbasit", "Lanre", "Steph", "Zara", "Stephen"]
    for i in names:
        queue.insert(i)
    print("Queue before removal: ")
    print(queue)
    print("Queue after removal: ")
    result = queue.empty_queue()
    print(result)
    print()
    
    print("Testing Equality in Queue")
    queue1 = QueueArray(6)
    queue2 = QueueArray(6)
    for i in range(5):
        queue1.insert(i)
    for j in range(5):
        queue2.insert(j)
        
    result = equals(queue1, queue2)
    print(result)
    print()
    
    print("Testing Reverse Queue Content")
    queue = QueueArray(20)
    queuecontent = ["Abdulbasit", "Stephen", "Joe", "TOE", "Bill"]
    for val in queuecontent:
        queue.insert(val)
    
    result = reverse_queue(queue)
    print(result)
    print()

if __name__ == "__main__":
    main()
    

    