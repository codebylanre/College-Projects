"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@mylaurier.ca
Section: CP164 Lab Fall 2023
__updated__ = "Oct 5, 2023"
------------------------------------------------------------------------
"""
from QueueArray import QueueArray



def plant_height_update(plantheight):
    new_height = QueueArray(20)
    
    while not plantheight.isEmpty():
        result = plantheight.remove()
        result += 2
        new_height.insert(result)
        
    return new_height

if __name__ == "__main__":
    
    def test():
        plantheights = [1, 2, 3, 4, 5]

        plantheight = QueueArray(30)
        
        for i in plantheights:
            plantheight.insert(i)
            
        result = plant_height_update(plantheight)
        print(result)
        

test()
        