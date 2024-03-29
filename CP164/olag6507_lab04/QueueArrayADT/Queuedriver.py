'''
Created on May 22, 2023

@author: Zara
'''

from QueueArray import QueueArray


def test_queue():
    
    Q1 = QueueArray(10)
    Q1.insert(20)
    Q1.insert("red")
    Q1.insert(39)
    
    print(Q1.printQueue())
    print()
    

test_queue()    