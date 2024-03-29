'''
Created on Sep 28, 2023

@author: abdulbasitolagunju
'''
from ArrayStack import ArrayStack
from Plant import Plant


def update_height(original_stack):
    
    updated_height = ArrayStack()
    
    while not original_stack.isEmpty():
        plant = original_stack.pop()
        plant += 2
        updated_height.push(plant)

    return updated_height
        
        
if __name__ == "__main__":
    
    original_stack = ArrayStack()
    
    plant = [10, 20, 30]
    
    for char in plant:
        original_stack.push(char)
        
    result = update_height(original_stack)

    while not result.isEmpty():
        plant = result.pop()
        print(plant)
        
        
    