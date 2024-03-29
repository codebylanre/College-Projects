"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Nov 14, 2023"
------------------------------------------------------------------------
"""

# THIS TASK IS IMPLEMENTED ON A DYNAMIC ARRAY
from DynamicArray import DynamicArray


class Array(DynamicArray):
    def removeDupes(self):
        new_items = []
        for i in range(self._n):
            if self._A[i] not in new_items:
                new_items.append(self._A[i])
        self._A = self._make_array(len(new_items))
        self._n = len(new_items)
        for i in range(self._n):
            self._A[i] = new_items[i]

    def display(self):
        for i in range(self._n):
            print(self._A[i], end=" ")
        print()

# Test code
testArray = Array()
testArray.append('bar')
testArray.append('put')
testArray.append('cat')
testArray.append('bar')
testArray.append('tea')
testArray.append('bar')
testArray.append('cat')
print("1. TEST ONE")
print("Original Array before sorting")
testArray.display()
print()

testArray.removeDupes()

print("Array after removing duplicates")
testArray.display()
print()
print()




"""
Since our new testArray no longer contains duplicates 
we would run our test Two with it to check how it handles 
arrays without duplicates
"""
print("2. TEST TWO")
print("Original Array without duplicates")
testArray.display()

testArray.removeDupes()

print()
print("Array without Duplicates (Remains unchanged) ")
testArray.display()
print()