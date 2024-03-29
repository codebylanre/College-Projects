'''
Created on Jun. 18, 2023

@author: Zara
'''
from LinkedQueue import LinkedQueue

if __name__=="__main__":
    
    Q1=LinkedQueue()
    
    Q1.enqueue(12)
    Q1.enqueue(20)
    Q1.enqueue(33)
    
    print(Q1.len()) 
    
    # print(Q1.top())
    print(Q1.dequeue())
    print(Q1.dequeue())
    print(Q1.dequeue())