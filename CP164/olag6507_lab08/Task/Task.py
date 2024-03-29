"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Nov 2, 2023"
------------------------------------------------------------------------
"""
from SinglyLinkedList import SinglyLinkedList
import time



print()
print("Sum Digits with Recursion")
def sum_digits(n):
    if n < 10:
        return n
    else:
        rem = n % 10
        digits = n // 10
        return rem + (sum_digits(digits)) 

print(sum_digits(56))

print()
print("Find minimum value with recursion")

def min_list(list_of_numbers):
    if len(list_of_numbers) == 1:
        return list_of_numbers[0]
    else:
        return min(list_of_numbers[0], min_list(list_of_numbers[1:]))
    

print(min_list([10, 5, 9, 8, 7, 4, 5]))

print()    
print("Fibonacci recursive with time calculation")
# Fibonacci function
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
# function to measure time
def measure_fibonacci_time(n):
    start_time = time.time()
    result = fibonacci(n)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


fib_calc = [10, 20, 30, 40, 50]

for n in fib_calc:
    result, execution_time = measure_fibonacci_time(n)
    print(f"Fibonacci({n}) = {result}, Execution Time: {execution_time:.6f} seconds")
"""
1. It takes time due to the numerous function call
2. Computing the higher numbers requires that the smaller numbers are computed again from the start
"""



def traverse(head):
    if (head == None):
        return
    # If head is not None, print current node
    # and recur for remaining list 
    else:
        print(head.data, end = " ")
        traverse(head.next)

def printReverse(listNode): 
  if listNode:
      printReverse(listNode.next)
      print(listNode.data, end = ' ')
  else:
      return