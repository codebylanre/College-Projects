'''
Created on Jul. 24, 2023

@author: 12265
'''
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