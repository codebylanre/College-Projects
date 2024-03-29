'''
Created on Jul. 24, 2023

@author: Abdulbasit
'''

import random

class Node:
    def __init__(self,key,value,next = None):
        self.key = key
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertAtFirst(self,key,value):
        self.head = Node(key,value,self.head)
        self.size += 1

    def insertAtLast(self,key,value):
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(key,value)
        self.size+=1

    def remove(self, key):
        current = self.head
        previous = None
        if current.key == key:
            self.head = current.next
        else:
            while current.next:
                previous = current
                current = current.next
                if current.key == key:
                    previous.next = current.next
            self.size -= 1

    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next

    def printAll(self):
        current = self.head
        while current:
            print(current.key,current.value)
            current = current.next

class HashTable:
    def __init__(self,size):
        self.table =[None] * size
        self.size = size

    def hashKey(self,key) -> int:
        """
            ord  -> built-in method that returns the Unicode code of a character 
            size -> the hash table length
            using (hashedString % self. size) -> for not getting an index out of the range of our  hash table length
        """
        hashedString = 0
        for character in key:
            hashedString += ord(character)
        return hashedString % self.size
    
    def hashKey_multiplication(self, key):
        """
        Multiplying the Unicode value with a chosen constant A,
        extracting the fractional part, and then multipplying by the size of hashTable
        The final hash value is obtained by taking the floor of the result
        """
        A = 0.343434
        hashedString = 0

        for characters in key:
            hashedString += ord(characters)

        hashedString *= A
        hashedString %= 1
        hashedString *= self.size

        return int(hashedString)
    
    def hashKey_midSquaremethod(self, key):
        """
        Key value is squared, the middle r digits are extracted as hash value
        The value r, is decided based on the size of the table
        in this case r is used as 2
        """

        hashedString = 0

        for characters in key:
            hashedString += ord(characters)
            
        squaredKey = int(hashedString) ** 2
        strSquaredKey = str(squaredKey)

        # Extract the middle digits if possible
        midIndex = len(strSquaredKey) // 2
        r = 2
        start = max(0, midIndex - r // 2)
        end = start + r

        hashedString = int(strSquaredKey[start:end])
        return hashedString % self.size



    def add(self, key, value):
        """
            The Logic:
            self.table[idx] is None 
                => create a linked list and insert into it a node that contains the giving key and the giving value
            self.table[idx] is not None:
                => insert into the linked list a node that contains the giving key and the giving value
        """
        idx = self.hashKey(key)
        if self.table[idx] is None:
            newLinkedList = LinkedList()
            newLinkedList.insertAtFirst(key,value)
            self.table[idx] = newLinkedList
        else:
            self.table[idx].insertAtLast(key, value)

    def add_multiplicationhash(self, key, value):
        """
            The Logic:
            self.table[idx] is None 
                => create a linked list and insert into it a node that contains the giving key and the giving value
            self.table[idx] is not None:
                => insert into the linked list a node that contains the giving key and the giving value
        """
        idx = self.hashKey_multiplication(key)
        if self.table[idx] is None:
            newLinkedList = LinkedList()
            newLinkedList.insertAtFirst(key,value)
            self.table[idx] = newLinkedList
        else:
            self.table[idx].insertAtLast(key, value)

    def add_midSqurehash(self, key, value):
        """
            The Logic:
            self.table[idx] is None 
                => create a linked list and insert into it a node that contains the giving key and the giving value
            self.table[idx] is not None:
                => insert into the linked list a node that contains the giving key and the giving value
        """
        idx = self.hashKey_midSquaremethod(key)
        if self.table[idx] is None:
            newLinkedList = LinkedList()
            newLinkedList.insertAtFirst(key,value)
            self.table[idx] = newLinkedList
        else:
            self.table[idx].insertAtLast(key, value)

    def get(self, key) -> any:
        idx = self.hashKey(key)
        if self.table[idx] is not None:
            return self.table[idx].find(key)

    def delete(self, key):
        idx = self.hashKey(key)
        if self.table[idx] is not None:
            self.table[idx].remove(key)

    def printAll(self):
        for i in self.table:
            if i is not None:
                i.printAll()

