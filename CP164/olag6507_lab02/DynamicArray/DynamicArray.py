'''
Created on Sep. 19, 2023

@author: Zara
'''

import ctypes # provides low-level arrays

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""
    def __init__(self):
        """Create an empty array."""
        self._n=0 # count actual elements
        self._capacity = 1 # default array capacity
        self._A = self._make_array(self._capacity) # low-level array

    def __len__ (self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__ (self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index' )
        return self._A[k] # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity: # not enough room
            self._resize(2*self._capacity) # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c): # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c) # new (bigger) array
        for k in range(self._n): # for each existing value
            B[k] = self._A[k]
        self._A=B # use the bigger array
        self._capacity = c

    def _make_array(self, c): # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)( ) # see ctypes documentation
    
    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity: # not enough room
            self._resize(2 * self._capacity) # so double capacity
        for j in range(self._n, k, -1): # shift rightmost first
            self._A[j] = self._A[j-1]
        self._A[k] = value # store newest element
        self._n += 1
        # I NEVER UNDERSTOOD THIS FOR LOOP ESPECIALLY BUT I GET THE IDEA
    
    def remove(self, value):
        """Remove the first occurence of value (or rause ValueError)"""
        # note: we do not consider shrinking the dynamics array in this version
        for k in range(self._n):
            if self._A[j] == value: # found a match!
                for j in range(k, self._n - 1): # shift others to fill gap
                    self._A[j] = self._A[j+1] 
                self._A[self._n - 1] = None  # help gabarge collcetion
                self._n -= 1    # We have one less item
                return # Exit immediately
            raise ValueError('Value not found')  # only reached if no match