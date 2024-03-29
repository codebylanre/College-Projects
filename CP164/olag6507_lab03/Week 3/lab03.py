"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Sep 28, 2023"
------------------------------------------------------------------------
"""
from ArrayStack import ArrayStack



def equal(stack_one, stack_two):    # Checks if a stack argument are completely equal
    """
    Function to check if two stacks are equal
    """
    print("LAB TASK 1")
    if (len(stack_one.data)) != (len(stack_two.data)):  #  Check if stack arguments have the same length
        return False
    while not stack_one.isEmpty():  
        if stack_one.pop() != stack_two.pop():  # Compare each content of the stacks if they are equal
            return False
    
    return True


def pythonlist_to_stack(list, stack):   
    """
    Appends a list item to a stack
    """

    stack = ArrayStack()    # Creating an empty stack
    print("LAB TASK 2")
    for i in list:
        stack.push(i)
    return stack
        
             
def append_stack(stack1, stack2): # Arguments must be stacks
    """
    Adds two stacks together (The method appends the content
    of second stack to the contents of the first stack in such
    a way that the content of first stack are at the top and 
    second stack come after it)
    """
     
     
    print("LAB TASK 3")
    result_stack = ArrayStack()


    while not stack1.isEmpty():             # Loops till stack is empty
        result_stack.push(stack1.pop())      

    while not stack2.isEmpty():
        result_stack.push(stack2.pop())

   
    reversed_stack = ArrayStack()           # Reversing the stack to maintain it original order
    while not result_stack.isEmpty():
        reversed_stack.push(result_stack.pop())

    return reversed_stack


def stutter(stackint): # Arguments should be stacks of integers
    """
    Creates a duplicate of each stack object and output a new stack
    replaces every value of stack
    with two occurrences of that value
    """
   
    print("LAB TASK 4")
    
    stutter_stack = ArrayStack() # Temporary stack
    
    while not stackint.isEmpty():
        content = stackint.pop()
        
        # Push it twice
        stutter_stack.push(content)
        stutter_stack.push(content)
           
    # Reverse temp stack
    
    reversed_stack = ArrayStack()
    while not stutter_stack.isEmpty():
        reversed_stack.push(stutter_stack.pop())
    
    return reversed_stack
    

    
    def plantstack():
        print("LAB TASK 5")
    

def main():
    print("1. Testing Equal Method")
    nums = [1, 2, 3, 4, 5]
    nums2 = [2, 4, 5, 6]
    stack1 = ArrayStack()
    stack2 = ArrayStack()
    
    for i in nums:
        stack1.push(i)
        
    for i in nums2:
        stack2.push(i)
        
    result = equal(stack1, stack2)
    print(f"Are the stacks equal? {result}")
    print()
    

    print("2. Testing Pythonlist_to_stack")
    list = [1, 2, "hello", "Hiiii", 3, 4]
    stack = []
    result = pythonlist_to_stack(list, stack)
    print(result)
    print()
    
    print("3. Testing Append stack")
    stack1 = ArrayStack()
    stack2 = ArrayStack()
    
    # Using numbers cause it easier to read the output
    for i in range(4):
        stack1.push(i)
    for ii in range(4, 9):
        stack2.push(ii)
    
    result = append_stack(stack1, stack2)
    print(result)
    print()
    
    print("4. Testing stutter")
    
    stackint = ArrayStack()
    stackint.push(3)
    stackint.push(7)
    stackint.push(1)
    stackint.push(14)
    stackint.push(9)
    result = stutter(stackint)
    print(result)
    print()
    
    # stackint, reversed_stack = stutter(stackint)
    # print("Normal stack: ", stackint)
    # print("Reversed stack: ", reversed_stack)





if __name__ == "__main__":
    main()


    

    