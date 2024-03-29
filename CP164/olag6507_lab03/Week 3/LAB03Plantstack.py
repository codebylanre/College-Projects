"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Sep 29, 2023"
------------------------------------------------------------------------
"""


from ArrayStack import ArrayStack
from Plant import Plant



        
def update_plant_heights(original_stack):
    updated_stack = ArrayStack()
    
    
    # Iterate through original stack, update height
    while not original_stack.isEmpty():
        plant = original_stack.pop()
        plant += 2
        updated_stack.push(plant)
        
    return updated_stack






if __name__ == "__main__":
    # TESTING THE CODE
    # Create a stack of plant objects
    plant_stack = ArrayStack()
    
    # Push plant objects onto the stack
    plants = [10, 20, 30]
    for plant in plants:
        plant_stack.push(plant)
    
    # Update the plant heights and store them in another stack
    updated_plant_stack = update_plant_heights(plant_stack)
    
    
    # Display plant height
    while not updated_plant_stack.isEmpty():
        plant = updated_plant_stack.pop()
        print(f"Updated plant height: {plant}")











