'''
Created on Jul. 9, 2023

@author: zara
'''

class Node(object):         # A node in a binary search tree
    def __init__(              # Constructor takes a key that is
        self,                # used to determine the position
        key,                 # inside the search tree,
        data,                # the data associated with the key
        left=None,           # and a left and right child node
        right=None):         # if known
        self.key  = key         # Copy parameters to instance
        self.data = data        # attributes of the object
        self.leftChild = left
        self.rightChild = right

    def __str__(self):         # Represent a node as a string
        return "{" + str(self.key) + ", " + str(self.data) + "}"
