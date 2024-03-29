"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Oct 19, 2023"
------------------------------------------------------------------------
"""

from LinkedStack import LinkedStack
from Plant import Plant


def pythonlist_to_Stack(list_plant, empty_stack):
    for plant in list_plant:
        empty_stack.push(plant)
    
    return empty_stack


def equal(stack1, stack2):
    if len(stack1) != len(stack2):
        return f"Equal: {False}"
    
    while not stack1.is_empty():
        if stack1.pop() != stack2.pop():
            return f"Equal: {False}"
    
    return f"Equal: {True}"


def reverse_linked_stack(stack):
    current = stack.head
    prev = None

    while current:
        next_node = current.get_next()
        current.set_next(prev)
        prev = current
        current = next_node

    stack.head = prev

    return stack
        
def stutter_linked(stack):
    temp_stack = LinkedStack()
    

    while not stack.is_empty():
        item = stack.pop()
        temp_stack.push(item)
        temp_stack.push(item)

    Reversed_stack = LinkedStack()
    while not temp_stack.is_empty():
        item = temp_stack.pop()
        Reversed_stack.push(item)

    # Reverse the linked stack
    while not Reversed_stack.is_empty():
        stack.push(Reversed_stack.pop())


        
    return stack
    

def main():
    print("Testing Task 1")
    
    # Create series of plant objects
    list_plant = [
        Plant("Rose", "Shrub", 30, "Moderate"),
        Plant("Tulip", "Wildflower", 15, "Low"),
        Plant("Maple", "Vine", 120, "High")
    ]
   
    # Create an emptystack object
    empty_stack = LinkedStack()
    
    pythonlist_to_Stack(list_plant, empty_stack)
    # Display item in stack
    while not empty_stack.is_empty():
        plant = empty_stack.pop()
        print(plant)
    
    print()
    
    print("Testing Task 2")
    stack1 = LinkedStack()
    stack2 = LinkedStack()

    for i in range(5):
        stack1.push(i)
    for i in range(2, 6):
        stack2.push(i)

    print(equal(stack1, stack2))
    
    print()
    
    print("Testing Task 3")
    
    stack = LinkedStack()
    for i in range(5):
        stack.push(i)
        
    reverse_linked_stack(stack)
    
    print("Original Stack")
    current = stack.head
    while current:
        print(current.data, end=" -> ")
        current = current.get_next()
    print("End")
    
    # Reverse the stack 
    reverse_linked_stack(stack)
    
    # Display the reversed stack
    print("Reversed Stack:")
    current = stack.head
    while current:
        print(current.data, end=" -> ")
        current = current.get_next()
    print("End")

    print()
    
    print("Testing Task 4")
    s = LinkedStack()

    print("Original Stack")
    for i in range(1, 7):
        s.push(i)
        print(i, end= " -> ")
    print("End")

    print("Edited Stack")
    stutter_linked(s)
    while not s.is_empty():
        item = s.pop()
        print(item, end=" -> ")
    print("End")




if __name__ == "__main__":
    main()



