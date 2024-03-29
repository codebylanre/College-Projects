'''
Created on Jul. 9, 2023

@author: zara, Abdulbasit 
'''

from Node import Node

class BinarySearchTree(object): # A binary search tree class
    def __init__(self):          # The tree organizes nodes by their
        self.__root = None        # keys. Initially, it is empty.
    
    def isEmpty(self):            # Check for empty tree
        return self.__root is None
    
    def root(self):               # Get the data and key of the root node
        if self.isEmpty():         # If the tree is empty, raise exception
            raise Exception("No root node in empty tree")
        return (                   # Otherwise return root data and its key
         self.__root.data, self.__root.key)
    
    
    def __find(self, goal):                 # Find an internal node whose key
        current = self.__root                # matches goal and its parent. Start at
        parent = self                        # root and track parent of current node
        level = 0                           # Initialize the level variable
        
        while (current and                   # While there is a tree left to explore
            goal != current.key):         # and current key isn't the goal
            parent = current                 # Prepare to move one level down
            current = (                      # Advance current to left subtree when
             current.leftChild if goal < current.key else # goal is
             current.rightChild)           # less than current key, else right

            level += 1                      # Increment the level during each iteration

        # If the loop ended on a node, it must have the goal key
        return (current, parent, level)            # Return the node or None and parent

    def search(self, goal):                # Public method to get data associated
        node, p, level = self.__find(goal)         # with a goal key. First, find node
        return node.data if node else None, level  # w/ goal & return any data
    
    def insert(self,                          # Insert a new node in a binary
              key,                            # search tree finding where its key
              data):                          # places it and storing its data
        node, parent, level = self.__find(             # Try finding the key in the tree
         key)                                 # and getting its parent node
        if node:                                # If we find a node with this key,
            node.data = data                     # then update the node's data
            return False                         # and return flag for no insertion

        if parent is self:                      # For empty trees, insert new node at
            self.__root = Node(key, data) # root of tree
        elif key < parent.key:            # If new key is less than parent's key,
            parent.leftChild = Node(      # insert new node as left
            key, data, right=node)            # child of parent
        else:                                   # Otherwise insert new node as right
            parent.rightChild = Node(     # child of parent
            key, data, right=node)
        return True                             # Return flag for valid insertion
    
    def delete(self, goal):                  # Delete a node whose key matches goal
        node, parent, level = self.__find(goal) # Find goal and its parent
        if node is not None:                  # If node was found,
            return self.__delete(              # then perform deletion at node
            parent, node), level                   # under the parent

    def __delete(self,                       # Delete the specified node in the tree
                 parent, node):              # modifying the parent node/tree
        deleted = node.data                   # Save the data that's to be deleted
        if node.leftChild:                    # Determine number of subtrees
            if node.rightChild:                # If both subtrees exist,
                self.__promote_successor(       # Then promote successor to
               node)                        # replace deleted node
            else:                              # If no right child, move left child up
                if parent is self:              # If parent is the whole tree,
                    self.__root = node.leftChild # update root  
                elif parent.leftChild is node:  # If node is parent's left,
                    parent.leftChild = node.leftChild # child, update left
                else:                           # else update right child
                    parent.rightChild = node.leftChild
        else:                                 # No left child; so promote right child
            if parent is self:                 # If parent is the whole tree,
                self.__root = node.rightChild   # update root
            elif parent.leftChild is node:     # If node is parent's left
                parent.leftChild = node.rightChild # child, then update
            else:                              # left child link else update
                parent.rightChild = node.rightChild # right child
        return deleted                        # Return the deleted node's data
    
    def __promote_successor(            # When deleting a node with both subtrees,
         self,                         # find successor on the right subtree, put
                                       # its data in this node, and delete the
         node):                        # successor from the right subtree
        successor = node.rightChild      # Start search for successor in
        parent = node                    # right subtree and track its parent
        while successor.leftChild:         # Descend left child links until
            parent = successor            # no more left links, tracking parent
            successor = successor.leftChild
        node.key = successor.key         # Replace node to delete with
        node.data = successor.data       # successor's key and data
        self.__delete(parent, successor) # Remove successor node
        
    def print(self,                      # Print the tree sideways with 1 node
             indentBy=4):               # on each line and indenting each level
      self.__pTree(self.__root,         # by some blanks. Start at root node
                   "ROOT:   ", "", indentBy) # with no indent

    def __pTree(self,                    # Recursively print a subtree, sideways
               node,                    # with the root node left justified
               nodeType,                # nodeType shows the relation to its
               indent,                  # parent and the indent shows its level
               indentBy=4):             # Increase indent level for subtrees
        if node:                          # Only print if there is a node
            self.__pTree(node.rightChild, "RIGHT:  ", # Print the right
                      indent + " " * indentBy, indentBy) # subtree
            print(indent + nodeType, node) # Print this node
            self.__pTree(node.leftChild,  "LEFT:   ", # Print the left
                      indent + " " * indentBy, indentBy) # subtree
            

# BINARY SEARCH TREE TASKS STARTS HERE
    def getSmallest_Iteration(self):
        if self.isEmpty():
            raise Exception("This node does not have a left child")
        
        current = self.__root
        parent = self
        # level = 0

        
        while current.leftChild:        # Smartest way to transverse to the left instead of Current != None
            parent = current
            current = current.leftChild
            # level += 1

        return (current.data, current.key)#, level
    

    def getLargest_Iteration(self):
        if self.isEmpty():
            raise Exception("This node does not have a right child")
        
        current = self.__root
        parent = self


        while current.rightChild:
            current = current.rightChild

        return (current.data, current.key)


    def getSmallest_Recursive(self):
        if self.isEmpty():
            raise Exception("This node does not have a left child")

        # Run recursion from root
        return self.__getSmallest_Recursive(self.__root)
    
    def __getSmallest_Recursive(self, current):
        # Base case: If there is no left child, then this is the smallest node
        if current.leftChild is None:
            return current.key, current.data
        
        # Recursive case: Traverse to the left child
        return self.__getSmallest_Recursive(current.leftChild)
    
    def getLargest_Recursive(self):
        if self.isEmpty():
            raise Exception("This node does not have a right child")
        
        # Run recursion from root
        return self.__getLargest_Recursive(self.__root)
        
    def __getLargest_Recursive(self, current):
        # Base case: if no right child, this is largest node
        if current.rightChild is None:
            return current.key, current.data
        
        # Recursive case: Traverse to the right child
        return self.__getLargest_Recursive(current.rightChild)
    
    def Ancestors(self, key):
        node, _, _ = self.__find(key)
        if not node:
            print(f"No node with key {key} found in the tree.")
            return

        self.__print_Ancestors(self.__root, key)

    def __print_Ancestors(self, root, key):
        if not root:
            return False

        if (
            (root.leftChild and root.leftChild.key == key) or
            (root.rightChild and root.rightChild.key == key) or
            self.__print_Ancestors(root.leftChild, key) or
            self.__print_Ancestors(root.rightChild, key)
        ):
            print(root.key)
            return True

        return False
    
        def Ancestors(self, key):
            if self.isEmpty():
                raise Exception("Tree is Empty")
            
            # Find node with given key and its parent
            node, parent = self.__find(key)

            if not node:
                raise Exception(f"Node with key: {key} not found")
            
            # print ancestors in reverse order
            self.__printAncestors(node, parent)

        def __printAncestors(self, node, parent):
            if parent is None:
                # Reached the root, exit recursion
                return
            else:
                # Recursively print ancestors
                self.__printAncestors(parent, self.__find(parent.key)[1])

                # Print the current ancestor
                print(parent.key, end=" ")



            # Unpack the tuple returned by __find
            current, new_parent = self.__find(parent.key)
            # Recursively print ancestors
            self.__printAncestors(current, new_parent)

            # Print the current ancestor
            print(parent.key, end= " ")