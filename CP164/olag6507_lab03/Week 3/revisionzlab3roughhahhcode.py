'''
Created on Sep 28, 2023

@author: abdulbasitolagunju
'''

from ArrayStack import ArrayStack

def equals(stack1, stack2):
    print("LAB TASK 2")
    print()
    if ( len(stack1) != len(stack2) ):
        return False
    
     
    while not stack1.isEmpty():
        if (stack1.pop() != stack2.pop() ):
            return False
        
    return True

def pythonlist_to_stack(list_string, empty_stack):
    print("LAB TASK 2")
    print()
    empty_stack = ArrayStack()
    for item in list_string:
        empty_stack.push(item)

def append_stack(int1, int2):
    print("LAB TASK 3")
    print()
    
    temp_stack = ArrayStack()
    
    while not int1.isEmpty():
        temp_stack.push(int1.pop())
        
    while not int2.isEmpty():
        temp_stack.push(int2.pop())
        
    
    reversed_stack = ArrayStack()
    while not temp_stack.isEmpty():
        reversed_stack.push(temp_stack.pop())
        
def stutter(stack_int):
    temp_updated_stack = ArrayStack()
    
    while not stack_int.isEmpty():
        temp_updated_stack.push(stack_int.pop())
        temp_updated_stack.push(stack_int.pop())
        
        reversed_updated_stack = ArrayStack()
        while not temp_updated_stack.isEmpty():
            reversed_updated_stack.push(temp_updated_stack.pop())
            
    return reversed_updated_stack

def main():
    print("seee")
    # equals(stack1, stack2)
    
    # pythonlist_to_stack(list_string, empty_stack)
    
    # append_stack(int1, int2)
    
    # stutter(stack_int)


if __name__ == "__main__":
    main()
    
    
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        