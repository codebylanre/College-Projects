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
from QueueArray import QueueArray

class ParcelGameSimulation:
    def pass_the_parcel(self, list_names, constant): # Constant represents number of movement
        sim_queue = QueueArray(len(list_names))
        
        # Insert the names into queue
        for name in list_names:
            sim_queue.insert(name)

        # The game process starts here  
        while len(sim_queue) > 1: # This leaves a winner
            for i in range(constant - 1):
                person = sim_queue.remove()
                sim_queue.insert(person)

            # disqualifies the person in front after the movements
            sim_queue.remove()

        # return winner
        return f"The winner is: {sim_queue.peek()}"
    
