'''
Created on Nov. 25, 2023

@author: Abdulbasit 
'''


from LinkedPriorityQueue import PriorityQueue

pq = PriorityQueue()

pq.enqueue(13,1)
pq.enqueue(15,1)
pq.enqueue(17,5)
pq.enqueue(4,2)

print()
print("Priority Queue:")
pq.display()

pq.enqueue(7, 2)

print("\nPriority Queue after enqueue:")
pq.display()

print("\nPeek:", pq.peek())

print("\nDequeue:", pq.dequeue())
print("Priority Queue after dequeue:")
pq.display()