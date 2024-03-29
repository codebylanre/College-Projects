"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Oct 20, 2023"
------------------------------------------------------------------------
"""

class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)
        # self.items.insert(-1, item) this works the same as the append


        # which side says front could be controversial
        # So, I added front to right to fit the figure

    def add_rear(self, item):
        self.items.insert(0, item)
        # which side says front could be controversial
        # So, I added rear to left to fit the figure
        # it's sometimes confusing

        
    def remove_front(self):
        return self.items.pop()
    
    def remove_rear(self):
        return self.items.pop(0)
    
    def is_empty(self):
        result = len(self.items) == 0
        return f"Empty: {result}"
    
    def size(self):
        count = 0
        for i in range(len(self.items)):
            count += 1
        return f"Size: {count}"
    
    # THis wasn't part of the task but i made it for fun
    def display(self):
        return self.items
