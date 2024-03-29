'''
Created on Jul. 24, 2023

@author: 12265
'''
from sortArray import Array
import timeit

if __name__=='__main__':
    arr = Array(5) 
    arr.insert(8)
    arr.insert(2)
    arr.insert(6)
    arr.insert(4)
    arr.insert(5)
    
    print(arr)
    
    arr.selectionSort()   
    print(arr)